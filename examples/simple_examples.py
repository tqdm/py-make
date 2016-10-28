import pymake


def main():
    """
    Execute pymake in the current working directory with sys.argv

    An explicit alternative:

    import subprocess
    subprocess.Popen("pymake",
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT).communicate()[0].decode('utf-8')

    Or just install py-make and run pymake in this directory.
    """
    pymake.main()


if __name__ == "__main__":
    main()
