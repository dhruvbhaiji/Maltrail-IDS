from core.common import retrieve_content

__url__ = "https://report.cs.rutgers.edu/DROP/attackers"
__check__ = ".1"
__info__ = "known attacker"
__reference__ = "rutgers.edu"

def fetch():
    retval = {}
    content = retrieve_content(__url__)

    if __check__ in content:
        for line in content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#') or '.' not in line:
                continue
            retval[line] = (__info__, __reference__)

    return retval
