import shutil
from setuptools import setup
import distutils.command.check

class TestCommand(distutils.command.check.check):
    """ test command """

    def run(self):

        import doctest

        from MONarchy import MONarchy

        print("======================")
        print("Runs test command ...")

        doctest.testmod(MONarchy)
        print('MONarchy module')

        distutils.command.check.check.run(self)

setup(
    name='MONarchy',
    version='1.0.0',
    maintener='Samuel DELEPOULLE',
    maintener_email='samuel.delepoulle@univ-littoral.fr',
    license='MIT',
    packages=['MONarchy'],
    install_requires=[
        'numpy'
    ],
    cmdclass={
        'test': TestCommand,
    },
    zip_safe=False
)