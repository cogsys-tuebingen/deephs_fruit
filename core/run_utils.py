import subprocess
import os


def get_current_git_hash():
    try:
        hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip()
        return str(hash.decode('ascii'))
    except:
        pass

    return "XXXX"


def get_slurm_job_id():
    import socket
    return str(os.environ.get('SLURM_JOB_ID', "%s:%s" % (socket.gethostname(), os.getcwd())))


def get_pip_packages():
    try:
        from pip._internal.operations import freeze
    except ImportError:  # pip < 10.0
        from pip.operations import freeze

    return list(freeze.freeze())


if __name__ == '__main__':
    print("Current git commit id is: %s" % get_current_git_hash())
    print("Current slurm job id: %s" % get_slurm_job_id())
    print("Installed pip packages: %s" % get_pip_packages())
