import time, os # Time for the delay, os to center the text

wait = 0.1 # Delay between each line
width = os.get_terminal_size().columns # Width of the console

# Clear the screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Intro
def intro():
    print(r"""         _               _      _        _          _                _         _                       _        """.center(width))
    time.sleep(wait)
    print(r"""        /\ \            _\ \   /\ \     /\_\       /\ \             /\ \      /\_\                    / /\      """.center(width))
    time.sleep(wait)
    print(r"""       /  \ \          /\__ \  \ \ \   / / /       \_\ \           /  \ \    / / /         _         / /  \     """.center(width))
    time.sleep(wait)
    print(r"""      / /\ \ \        / /_ \_\  \ \ \_/ / /        /\__ \         / /\ \ \   \ \ \__      /\_\      / / /\ \__  """.center(width))
    time.sleep(wait)
    print(r"""     / / /\ \_\      / / /\/_/   \ \___/ /        / /_ \ \       / / /\ \_\   \ \___\    / / /     / / /\ \___\ """.center(width))
    time.sleep(wait)
    print(r"""    / /_/_ \/_/     / / /         \ \ \_/        / / /\ \ \     / / /_/ / /    \__  /   / / /      \ \ \ \/___/ """.center(width))
    time.sleep(wait)
    print(r"""   / /____/\       / / /           \ \ \        / / /  \/_/    / / /__\/ /     / / /   / / /        \ \ \       """.center(width))
    time.sleep(wait)
    print(r"""  / /\____\/      / / / ____        \ \ \      / / /          / / /_____/     / / /   / / /     _    \ \ \      """.center(width))
    time.sleep(wait)
    print(r""" / / /______     / /_/_/ ___/\       \ \ \    / / /          / / /\ \ \      / / /___/ / /     /_/\__/ / /      """.center(width))
    time.sleep(wait)
    print(r"""/ / /_______\   /_______/\__\/        \ \_\  /_/ /          / / /  \ \ \    / / /____\/ /      \ \/___/ /       """.center(width))
    time.sleep(wait)
    print(r"""\/__________/   \_______\/             \/_/  \_\/           \/_/    \_\/    \/_________/        \_____\/        """.center(width))
    time.sleep(wait)
    print("\n") # A new line doesn't work with .center :(
    print("Studios".center(width))
    time.sleep(3)
    clear() # Clears the console for the next text