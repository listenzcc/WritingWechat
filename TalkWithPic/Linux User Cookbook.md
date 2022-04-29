## Linux User Cookbook

<aside>
💡 To whom wants to, but never got a chance to try Linux Server.

</aside>

## Quick Start

- [ ]  🌐Download & Install MobaXterm
- [ ]  🙂Ask admin to make you account (Login IP, Username, Password)
- [ ]  🤖Establish the remote session of MobaXterm to log in the server with SSH
- [ ]  ⌨️(Optional) Establish the remote development environment with VSCode or Pycharm or something like
- [ ]  🆗(Optional) Set up your Key Authorization of SSH login without password

---

## Client in PC end

MobaXterm provides the State-of-Art experience of operating a remote-based Linux Server in your PC Client.

[MobaXterm free Xserver and tabbed SSH client for Windows](https://mobaxterm.mobatek.net/)

For personal use, the **FREE** version is enough.

## Authorization & Login

- Ask your Linux Server administrator to make you the environment.
    - You will need the username, password, home directory and login shell.
- Make sure he or she enables your account with SSH login permission.

## Setup SSH connection with MobaXterm

The MobaXterm provides one-stand initializing with SSH.

1. Links to the remote host

![Untitled](Untitled.png)

1. Choose a Terminal Type

Basically, it makes the terminal more colorful

![Untitled](Untitled%201.png)

1. Setup proxy if necessary

![Untitled](Untitled%202.png)

1. Tell the MobaXterm to remember the session as the session name

![Untitled](Untitled%203.png)

1. Login with the username and password.

![Untitled](Untitled%204.png)

After you input the username and press **Enter**, the password area will give **no** feedback as you type.

It is OK, just type it and press **Enter** to submit.

The session will automatically remember your password, that means

- The next time you log in with the session, you are exempt to submit the username and password;
- If you want to log in with another username, you have to establish another session or uncheck the username in the step-1;
- If the password fails for some reason, the login prompt will show again and ask to input the password again.

## Shell

The shell is the main interaction between you and the server through terminal.

[Introduction to Linux Shell and Shell Scripting - GeeksforGeeks](https://www.geeksforgeeks.org/introduction-linux-shell-shell-scripting/)

> If you are using any major operating system you are indirectly interacting to **shell**. If you are running Ubuntu, Linux Mint or any other Linux distribution, you are interacting to shell every time you use terminal. In this article I will discuss about linux shells and shell scripting so before understanding shell scripting we have to get familiar with following terminologies – Kernel, Shell, Terminal.
>

![https://media.geeksforgeeks.org/wp-content/uploads/18834419_1198504446945937_35839918_n-300x291.png](https://media.geeksforgeeks.org/wp-content/uploads/18834419_1198504446945937_35839918_n-300x291.png)

## Remote Development using SSH

### VSCode

Alternative, if you program, the VSCode works with the server in remote.

The connection also uses SSH.

Just follow the guide to play with it.

[Developing on Remote Machines using SSH and Visual Studio Code](https://code.visualstudio.com/docs/remote/ssh)

![https://code.visualstudio.com/assets/docs/remote/ssh/architecture-ssh.png](https://code.visualstudio.com/assets/docs/remote/ssh/architecture-ssh.png)

### Pycharm

If you are a Pycharm user, it provides the similar method

[Configure an interpreter using SSH | PyCharm](https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html)

## SSH without password

For you who

- forget your password a lot
- don’t want to type the password all the time
- want to enhance the login security

You can use Key Authentication method to replace the password.

[How to use SSH keys for authentication](https://upcloud.com/community/tutorials/use-ssh-keys-authentication/#:~:text=%20How%20to%20use%20SSH%20keys%20for%20authentication,your%20own%20computer%20if%20you%20are...%20More%20)

[How to Use Public Key Authentication with SSH {Step-by-Step Guide}](https://phoenixnap.com/kb/ssh-with-key)

Be sure you update the key periodically, and delete it totally when you do not use the PC any longer.