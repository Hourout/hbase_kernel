import happybase
import pandas as pd
from ipykernel.kernelbase import Kernel


__version__ = '0.1.0'

class HbaseKernel(Kernel):
    implementation = 'hbase_kernel'
    implementation_version = __version__
    language = 'sql'
    language_version = 'latest'
    language_info = {'name': 'sql',
                     'mimetype': 'text/x-sh',
                     'file_extension': '.sql'}
    banner = 'hbase kernel'

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self.engine = False
        
    def output(self, output):
        if not self.silent:
            display_content = {'source': 'kernel',
                               'data': {'text/html': output},
                               'metadata': {}}
            self.send_response(self.iopub_socket, 'display_data', display_content)
    
    def ok(self):
        return {'status':'ok', 'execution_count':self.execution_count, 'payload':[], 'user_expressions':{}}

    def err(self, msg):
        return {'status':'error',
                'error':msg,
                'traceback':[msg],
                'execution_count':self.execution_count,
                'payload':[],
                'user_expressions':{}}

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
        self.silent = silent
        message = 'Unable to connect to Hbase server. Check that the server is running.'
        output = ''
        if not code.strip():
            return self.ok()
        sql = code.rstrip()+('' if code.rstrip().endswith(";") else ';')
        try:
            for v in sql.split(";"):
                v = v.rstrip()
                l = v.lower()
                if len(l)>0:
                    if l.startswith('hbase://'):
                        conn = v[8:].split(':')
                        self.engine = happybase.Connection(conn[0], int(conn[1]))
                    elif l.startswith('select '):
                        if not self.engine:
                            self.output(message)
                            return self.ok()
                        column = [i.strip() for i in v.split(' from ')[0][6:].split(',') if len(i.strip())>0]
                        table = self.engine.table(v.split(' from ')[1].strip())
                        scanner = table.scan(columns=column)
                        data = []
                        for r, (key, value) in enumerate(scanner):
                            value = {i.decode():j.decode() for i, j in value.items()}
                            if r>1000:
                                break
                            data.append(dict(**{'key':key.decode()}, **{col:value.get(col, '') for col in column}))
                        output = pd.DataFrame(data).to_html()
                    else:
                        output = 'Hbase SQL Syntax errors, please check SQL Syntax.'
            self.output(output)
            return self.ok()
        except Exception as msg:
            self.output(str(msg))
            return self.err('Error executing code ' + sql)
