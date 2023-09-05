# Python Screen Sharing Script

A Python script for screen sharing between a sender and a receiver using the VidStream library.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributions](#contributions)
- [License](#license)

## Introduction

This Python script allows you to share your screen between a sender and a receiver using the VidStream library. It enables real-time screen sharing, making it useful for various applications like remote collaboration, presentations, and more.

## Features

- Real-time screen sharing between a sender and a receiver.
- Easy setup and usage with the VidStream library.

## Requirements

To use this script, you need the following:

- Python 3.x
- The `threading` module (usually included in Python standard library)
- VidStream library (see how to install it below)
- An active network connection
- Two computers or instances to act as the sender and receiver

## Installation

1. Clone this repository or download the ZIP file and extract it to your preferred location on both the sender and receiver computers.

   ```bash
   git clone https://github.com/elcruzo/screen-sharing-python.git
   cd screen-sharing-python

2. Install the Vidstream Library.

   ```bash
   pip install vidstream

## Usage

Receiver (receiver.py)

1. Open a terminal or command prompt on the receiver computer.
2. Navigate to the project directory where the `receiver.py` script is located.
3. Run the receiver script, providing the sender's IP address:

   ```bash
   python receiver.py

Sender (sender.py)

1. Open a terminal or command prompt on the sender computer.
2. Navigate to the project directory where the `sender.py` script is located.
3. Run the sender script:

   ```bash
   python sender.py
4. The sender will display its IP address. This is the IP address that shoud be shared with the receiver.
5. The receiver will connect to the sender, and you will see the shared screen.
6. To stop screen sharing, press `ENTER` and type `STOP`.

## Contributions

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and commit them with descriptive commit messages.

4. Push your branch to your fork.

5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Have fun exploring my Screen Sharing tool! If you have any questions or run into issues, don't hesitate to ask for help.


