import os
import shutil
import importlib.util
import sys
import time
import webbrowser
import discord
import asyncio
import requests



color_cycle = [
    "\033[91m",  
    "\033[92m",  
    "\033[93m",  
    "\033[94m",  
    "\033[95m",  
    "\033[96m",  
    "\033[97m",  
]
reset = "\033[0m"

ascii_art = [
    "███████╗███████╗ ██████╗██████╗ ███████╗████████╗",
    "██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝",
    "███████╗█████╗  ██║     ██████╔╝█████╗     ██║   ",
    "╚════██║██╔══╝  ██║     ██╔══██╗██╔══╝     ██║   ",
    "███████║███████╗╚██████╗██║  ██║███████╗   ██║   ",
    "╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ",
]

def slow_print(text, delay):
    """Print text slowly, character by character."""
    for char in text:
        print(char, end='', flush=True)  
        time.sleep(delay)  
    print()  

def print_centered(text, width):
    """Print the text centered."""
    for line in text:
        print(line.center(width))

def show_loading_screen():
    """Show animated loading screen with color cycling for both ASCII and the loading bar."""
    width = os.get_terminal_size().columns
    for i in range(1, 101):
        os.system('cls' if os.name == 'nt' else 'clear')

        color_index = i % len(color_cycle)
        current_color = color_cycle[color_index]
        
        colored_ascii = [current_color + line + reset for line in ascii_art]
        print_centered(colored_ascii, width)

        filled_length = i // 2
        bar = f"{current_color}Loading: [{('=' * filled_length).ljust(50)}] {i}%{reset}"
        print_centered([bar], width)

        time.sleep(0.05)  

    os.system('cls' if os.name == 'nt' else 'clear')
    slow_print("Ty for using this tool. Going to the main menu", 0.05)  
    time.sleep(2)


os.system("title Multi tool🤓 -- made by Bozo")
if __name__ == "__main__":
    show_loading_screen()

RESET = "\033[0m"
BOLD = "\033[1m"

color_options = {
    "1": {"name": "SKIDS", "code": "\033[95m"},
    "2": {"name": "Firestorm", "code": "\033[91m"},
    "3": {"name": "Solar Flare", "code": "\033[93m"},
    "4": {"name": "Emerald Rush", "code": "\033[92m"},
    "5": {"name": "Deep Blue", "code": "\033[94m"},
    "6": {"name": "Rose", "code": "\033[38;5;205m"},
    "7": {"name": "Cyan", "code": "\033[36m"},
    "8": {"name": "Water", "code": "\033[96m"},
    "9": {"name": "Orange", "code": "\033[38;5;208m"},
    "10": {"name": "Purple", "code": "\033[38;5;129m"}
}

current_theme = color_options["10"]["code"]

def print_centered(text, width):
    lines = text.split("\n")
    for line in lines:
        print(current_theme + line.center(width) + RESET)

PURPLE_GLOW = "\033[38;5;129m"  
DIM = "\033[2m"  
RESET = "\033[0m"

def print_options_box(width):
    box_width = max(60, width - 60)  
    border_top = '┌' + '─' * (box_width - 2) + '┐'
    border_bottom = '└' + '─' * (box_width - 2) + '┘'
    
    print(current_theme + border_top.center(width) + RESET)
    print(current_theme + f"| {'11: mass dm'.center(box_width)} |".center(width) + RESET)
    print(current_theme + f"| {'9: Funny bot 1'.center(box_width)} |".center(width) + RESET)
    print(current_theme + f"| {'10: GC Spammer '.center(box_width)} |".center(width) + RESET)
    print(current_theme + f"{'1: IP Puller'.center(box_width//2)}  {'2: Server Fucker🥱'.center(box_width//2)}".center(width) + RESET)
    print(current_theme + f"{'3: Skibidi Fucker🥰'.center(box_width//2)}  {'4: Set Theme🎫'.center(box_width//2)}".center(width) + RESET) 
    print(current_theme + f"{'5: Join Second Server👉'.center(box_width)}".center(width) + RESET)
    print(current_theme + f"{'8: Funny bot 2'.center(box_width)}".center(width) + RESET)
    print(current_theme + f"{'6: Join server'.center(box_width)}".center(width) + RESET)
    print(current_theme + f"{'12: Bio changer'.center(box_width)}".center(width) + RESET)
    print(current_theme + border_bottom.center(width) + RESET)
    
    

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay):
    """Print text slowly, character by character."""
    for char in text:
        print(char, end='', flush=True)  
        time.sleep(delay)  
    print()  

def set_theme():
    global current_theme
    while True:
        print("\nChoose a theme:\n")
        for key, value in color_options.items():
            print(f"{value['code']}{key}: {value['name']}{RESET}")

        theme_choice = input(current_theme + "Enter your choice: " + RESET)

        if theme_choice in color_options:
            selected_theme = color_options[theme_choice]
            current_theme = selected_theme['code']
            clear_screen()
            success_message = f"{current_theme}{selected_theme['name']} theme set successfully ✅.\n{RESET}"
            slow_print(success_message, 0.05)  
            time.sleep(1)  
            break
        else:
            slow_print(f"{current_theme}Invalid choice! Please try again.{RESET}", 0.05)
            time.sleep(2)


async def send_message_to_friend(token, user_id):
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'{current_theme}Bot is online as {client.user}{RESET}')
        while True:
            try:
                user = await client.fetch_user(user_id)
                message = input(f"{current_theme}Enter the message to send to the user (type 'exit' to stop): {RESET} ")
                if message.lower() == "exit":
                    print(f"{current_theme}Exiting message mode.✅{RESET}")
                    break
                await user.send(message)
                print(f"{current_theme}Successfully sent a message ✅{RESET}")
            except discord.NotFound:
                print(f"{current_theme}User ID not found. The bot needs to be in the server with the person like a server where your friend is in❌{RESET}")
                time.sleep(3)
                break
            except Exception as e:
                print(f"{current_theme}An error occurred❌: {e}{RESET}")
                time.sleep(3)
                break
        await client.close()

    await client.start(token)

async def send_message_as_bot(token, channel_id):
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'{current_theme}Bot is online as {client.user}{RESET}')
        try:
            channel = client.get_channel(int(channel_id))
            if channel is None:
                print(f"{current_theme}Invalid channel ID.🤞{RESET}")
                await client.close()
                return
            
            while True:
                message = input(f"{current_theme}Enter the message to send (or type 'exit' to quit): {RESET}")
                if message.lower() == 'exit':
                    break
                await channel.send(message)
                print(f"{current_theme}Message sent✅{RESET}")
        except Exception as e:
            print(f"{current_theme}An error occurred❌: {e}{RESET}")
        finally:
            await client.close()

def start_tool(option):
    tools_folder = "tools"
    
    tool_file_map = {
        "1": "ippuller.py",
        "2": "serverfucker.py",
        "3": "skibidifucker.py",
        "7": "secret.py",
        "10": "gcspammer.py",
        "11": "Massdm.py",
        "12": "Local.py",
    }

    tool_file = tool_file_map.get(option)
    if tool_file:
        tool_path = os.path.join(tools_folder, tool_file)
        if os.path.isfile(tool_path):
            print(f"{current_theme}Starting tool from {tool_file}...{RESET}")
            spec = importlib.util.spec_from_file_location("tool_module", tool_path)
            tool_module = importlib.util.module_from_spec(spec)
            sys.modules["tool_module"] = tool_module
            spec.loader.exec_module(tool_module)
            
            if hasattr(tool_module, 'run'):
                tool_module.run()
            else:
                print(f"{current_theme}Error: The tool '{tool_file}' does not have a 'run' function.{RESET}")
        else:
            print(f"Tool file {tool_file} does not exist.")
    elif option == "4":
        set_theme()
    elif option == "5":
        print(f"{current_theme}U cheating ):{RESET}")
        time.sleep(1)
        webbrowser.open("https://discord.gg/4nseXXEpQZ")  
    elif option == "6":
        print(f"{current_theme}R U LOYAL?{RESET}")
        time.sleep(1)
        webbrowser.open("https://discord.gg/dvbusPv9nB")
    elif option == "8":
        token = input(f"{current_theme}Enter your bot token: {RESET}")
        channel_id = input(f"{current_theme}Enter the channel ID: {RESET} ")
        asyncio.run(send_message_as_bot(token, channel_id))  
    elif option == "9":
        token = input(f"{current_theme}Enter your bot token: {RESET}")
        user_id = input(f"{current_theme}Enter the user ID: {RESET}")
        asyncio.run(send_message_to_friend(token, user_id)) 
    else:
        print(f"{current_theme}R u Retarded?🥴{RESET}")

def main():
    clear_screen()
    os.system("title Multi tool🤓 -- made by Bozo")

    while True:
        clear_screen()
        width = shutil.get_terminal_size().columns
        print_centered('''
████████╗██╗███╗   ███╗███╗   ███╗██╗   ██╗    ████████╗██╗   ██╗██████╗ ███╗   ██╗███████╗██████╗ 
╚══██╔══╝██║████╗ ████║████╗ ████║╚██╗ ██╔╝    ╚══██╔══╝██║   ██║██╔══██╗████╗  ██║██╔════╝██╔══██╗
   ██║   ██║██╔████╔██║██╔████╔██║ ╚████╔╝        ██║   ██║   ██║██████╔╝██╔██╗ ██║█████╗  ██████╔╝
   ██║   ██║██║╚██╔╝██║██║╚██╔╝██║  ╚██╔╝         ██║   ██║   ██║██╔══██╗██║╚██╗██║██╔══╝  ██╔══██╗
   ██║   ██║██║ ╚═╝ ██║██║ ╚═╝ ██║   ██║          ██║   ╚██████╔╝██║  ██║██║ ╚████║███████╗██║  ██║
   ╚═╝   ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝   ╚═╝          ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                                                                                                                                
DONT SKID LEARN CODING LIL BRO 
''', width)
        print_options_box(width)
        option = input(f"{current_theme} Enter tool | getdaddysmilk🤭: {RESET}")
        start_tool(option)

if __name__ == "__main__":
     main()