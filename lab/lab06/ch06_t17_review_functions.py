def shut_down(s: str) -> str:
    if s == "yes":
        return "Shutting down"
    elif s == "No":
        return "Shutdown aborted"
    else:
        return "Sorry"
