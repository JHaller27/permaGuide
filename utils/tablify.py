import sys
import re


TABLE_ROW_REGEX = re.compile(r"^([^|]+?)\s*\|\s*(\S+)\s*\|\s*(.*)$")


class StdIn:
    def __init__(self):
        self._had_data = False

    def __iter__(self):
        return self

    def __next__(self) -> str:
        data = input().strip()

        if self._had_data and data == "":
            raise StopIteration

        self._had_data = data != ""

        return data


class Data:
    def __init__(self, itr):
        self._curr = None
        self._itr = iter(itr)

    def next(self) -> str:
        try:
            return next(self._itr).strip()
        except StopIteration:
            self._curr = None
            return None

    def run(self, start):
        self._curr = start
        while self._curr is not None:
            self._curr = self._curr(self)


def end_state(ctx: Data):
    return None


def end_table(ctx: Data):
    print()
    print()

    return wait_for_title


def handle_table_row(ctx: Data):
    line = ctx.next()
    if line == "":
        return end_table

    mo = TABLE_ROW_REGEX.search(line)
    if mo is None:
        return end_state

    print(f"| **{mo[1]}** | `{mo[2]}` | {mo[3]} |")

    return handle_table_row


def start_table(ctx: Data):
    line = ctx.next()
    line = line.replace("\t", " ")
    print(f"| {line} |")

    ctx.next()
    print("|:--|:--|:--|")

    return handle_table_row


def wait_for_title(ctx: Data):
    data = ctx.next()
    if data != "":
        print(f"## {data}")
        ctx.next()

        return start_table

    return wait_for_title


def start(ctx: Data):
    if len(sys.argv) > 2:
        skip_to = int(sys.argv[2])
        for _ in range(skip_to-1):
            line = ctx.next()

    return wait_for_title


path = sys.argv[1]
if path == "-":
    lines = StdIn()
else:
    with open(path, "r") as fp:
        lines = [l for l in fp]

context = Data(lines)
context.run(start)
