import click
from pykeepass import PyKeePass
from pykeepass.exceptions import CredentialsError
import pyperclip



@click.command()
@click.option('--password', prompt="🔐 Please, enter the password", hide_input=True, required=False)
@click.option('--file', prompt="🔐 Please, enter the keys file", required=True)
def main(file,password):
    kp = None
    retries = 5

    while kp is None:
        if not password:
            password = click.prompt('🔐 Please, enter the password', hide_input=True)
        try:
            kp = PyKeePass(file, password=password)
        except CredentialsError:
            retries -= 1
            click.echo("\n❌ Wrong password, please try again.\n")
            password = None
            if retries == 0:
                click.echo("🚫 Maximum number of retries reached. Please try again later.")
                return
        except Exception as e:
            click.echo(f"⚠️ Unexpected error: {e}")
            return

    click.echo("\n" + "=" * 40)
    click.echo("✅ Successfully authenticated!")
    click.echo("=" * 40 + "\n")

    # Show groups
    group_list = []
    groups = kp.groups
    i = 0
    for group in groups:
        if group.entries and len(group.entries) > 0:
            click.echo(f"{i}️ {group.name} - {group.notes}")
            group_list.append(group.entries)
            i += 1

    # If no groups, we quit the program
    if not group_list:
        click.echo("🚫 There are no groups with entries. Exiting.")
        return

    click.echo("\n" + "-" * 40)
    choice = int(click.prompt("📁 Select the group to view its accounts"))
    users_list = group_list[choice]
    click.echo("-" * 40 + "\n")

    # Show users of the group
    passwd_list = []
    username_list = []

    for idx, entry in enumerate(users_list):
        click.echo(f"{idx}️ {entry.username}")
        passwd_list.append(entry.password)
        username_list.append(entry.username)


    # Select the user
    click.echo("\n" + "-" * 40)
    acc_choice = int(click.prompt("👤 Select the account to view its password"))
    pyperclip.copy(username_list[acc_choice])
    click.echo("-" * 40 + "\n")

    #Copy user
    click.echo(f"📋 Copied username: {username_list[acc_choice]}")
    click.echo("\n" + "=" * 40)


    #Copy pass
    input(" Press Enter to copy the password to clipboard ")
    click.echo("\n" + "=" * 40)

    pyperclip.copy(passwd_list[acc_choice])

    click.echo(f"🔑 Password copied")
    click.echo("\n" + "=" * 40)
    click.echo("🔒 Done. Stay safe.")
    click.echo("=" * 40 + "\n")

    #END


if __name__ == "__main__":
    main()
