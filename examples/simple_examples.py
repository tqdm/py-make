import pymake


def main():
    # execute pymake in the current working directory with sys.argv
    pymake.main()

    """
    # explicit alternative
    import subprocess
    subprocess.Popen("pymake",
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT).communicate()[0].decode('utf-8')
    """


if __name__ == "__main__":
    main()
