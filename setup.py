from setuptools import setup


def readme():
    with open('README.md', encoding='utf-8') as f:
        return f.read()

setup(name='hbase_kernel',
      version='0.1.0',
      description='A hbase kernel for Jupyter.',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/Hourout/hbase_kernel',
      author='JinQing Lee',
      author_email='hourout@163.com',
      keywords=['jupyter_kernel', 'hbase_kernel'],
      license='Apache License Version 2.0',
      install_requires=['happybase', 'pandas', 'jupyter'],
      classifiers = [
          'Framework :: IPython',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
          'Topic :: System :: Shells',
      ],
      packages=['hbase_kernel'],
      zip_safe=False
)