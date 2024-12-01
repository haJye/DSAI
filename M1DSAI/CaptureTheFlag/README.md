# Capture the Flag Multiagent System

## Project Overview

This project is a simulation of a Capture the Flag game implemented using a multiagent system. The system consists of two teams: the Blue team and the Red team, each composed of 5 agents. The objective of the game is for each team to capture the opposing team's flag while defending their own.

## Agents

### Blue Team
- Bob
- Bob2
- Bob3
- Bob4
- Bob5

### Red Team
- Rio
- Rio2
- Rio3
- Rio4
- Rio5

Each agent operates independently within the environment, making decisions based on its perception of the environment and predefined strategies.

## Game Rules

1. The game environment consists of a grid-based map with obstacles and two flags, one for each team.
2. Agents can move around the map, capture the flag of the opposing team.
3. Agents can also defend their flag by intercepting and tagging opponents who attempt to capture it.
4. The game ends when one team successfully captures the flag of the opposing team.


## Implementation Details

- The project is implemented using [Jason](http://jason.sourceforge.net/wp/) (Java-based AgentSpeak interpreter).
- You need to have Java 17 and Gradle installed to run the project.

## How to Run the Project

1. Install [Java 17](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) if you haven't already.
2. Install [Gradle](https://gradle.org/install/) if you haven't already.
3. Install Jason by following the instructions on the [Jason website](https://github.com/jason-lang/jason/releases).
4. Clone the project repository from [GitHub](https://github.com/haJye/CaptureTheFlag).
5. Navigate to the project directory in your terminal.
6. Run the following command to start the simulation:
   ```bash
   jason ctf.mas2j

## Contributors

- [Haji Akhundzada](https://github.com/haJye)
- [Ravan Iskandarov](https://github.com/i-revan)
- [Arzuman Hasanov](https://github.com/arzuman-hasanov)



