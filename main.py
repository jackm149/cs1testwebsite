from drafter import *
from dataclasses import dataclass

set_website_title("Jack's Test Website 09112026")
set_site_information(
    author="Jack Mallett",
    description="This is my description",
    sources="Drafter docs for the most part",
    planning="",
    links=["https://github.com/jackm149/cs1testwebsite/"]
)
hide_debug_information()
set_website_framed(False)

@dataclass
class State:
    count: int

@route
def index(state: State) -> Page:
    return Page(state, [
        "Current count: " + str(state.count) + "\n",
        Button("-1", "decrement"),
        Button("+1", "increment"),
        Button("+2", "increment2"),
        Button("Reset", "reset_count")
    ])

@route
def decrement(state: State) -> Page:
    if state.count >= 1:
        state.count = state.count - 1
    return index(state)

@route
def increment(state: State) -> Page:
    state.count = state.count + 1
    return index(state)

@route
def increment2(state: State) -> Page:
    state.count = state.count + 2
    return index(state)


@route
def reset_count(state: State) -> Page:
    state.count = 0
    return index(state)

start_server(State(4))
