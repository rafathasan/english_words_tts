# English Dictionary Words with Text-to-Speech (TTS) README

This Git repository is intended to help English learners expand their vocabulary by using a Text-to-Speech (TTS) tool to read out a list of English dictionary words.

## Getting Started

### Prerequisites

-   Docker: This project is designed to run using Docker, so you must have Docker installed on your computer before you can start.

### Installation

1.  Clone the repository to your local machine
2.  Navigate to the project directory using the terminal (`cd words-tts`)
3.  Type the following command to start the TTS: `docker-compose up`

### Usage

The project is designed to read out the list of words contained in the `words.txt` file. The TTS will begin reading out the words as soon as the project is started using the `docker-compose up` command.

## Repository Contents

-   `words.txt`: Contains a list of English dictionary words that will be read out by the TTS
-   `main.py`: The main Python script that runs the TTS
-   `Dockerfile`: The Docker configuration file used to build the Docker image for this project
-   `docker-compose.yaml`: The Docker Compose file used to start the Docker containers for this project

## Disclaimer

This project is only intended to be used as a tool for expanding your English vocabulary and should not be relied on as the sole method of preparation for English proficiency tests.

## Contributing

Contributions are welcome! Please feel free to submit a pull request if you have any improvements to suggest.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project for any purpose. However, the software is provided "as is" without warranty of any kind, express or implied. The author of this project shall not be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services, loss of use, data, or profits, or business interruption) arising in any way out of the use of this software, even if advised of the possibility of such damage.
