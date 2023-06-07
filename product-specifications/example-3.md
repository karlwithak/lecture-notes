# Project Specification: 'Maze Runner' CLI Game 🏃

## Overview

'Maze Runner' is a text-based, Command-Line Interface (CLI) game designed for users who appreciate the simplicity and challenge of classic text-based games. The main objective is to navigate a maze and find the exit as quickly as possible.

## Goals

1. To provide an engaging gaming experience to users who enjoy text-based games.
2. To challenge players with randomly generated mazes of varying complexity.
3. To include a scoring system based on maze complexity and completion time.

## Scope

The game will consist of the following components:

1. Maze Generation: Rules for generating mazes of different sizes and complexity.
2. User Interface: Text-based instructions and input prompts for player actions.
3. Scoring System: Based on maze complexity and completion time.

## Requirements

### Maze Generation

1. The game should be able to generate square mazes of different sizes, ranging from simple (e.g., 5x5 grid) to complex (e.g., 20x20 grid).
2. Each maze should have a randomly placed start point and end point.
3. Maze pathways and walls should be randomly generated, ensuring there is at least one valid path from the start to the end.

### User Interface

1. **Movement Instructions:** Players should receive clear instructions on how to move within the maze (e.g., "Enter 'N' for North, 'S' for South, 'E' for East, 'W' for West").
2. **Maze Display:** The current state of the maze should be displayed after each move, indicating the player's current position and the unseen parts of the maze.
3. **Completion Notification:** Upon reaching the end point, players should receive a message indicating they've successfully completed the maze.

### Scoring System

1. Players earn points based on the size and complexity of the maze and how quickly they find the exit.
2. The game should display the player's score upon maze completion.

## Technical Specifications

The game will be developed using Python, which has robust support for CLI applications. 

## Non-Functional Requirements

1. **Usability:** Despite being a CLI game, 'Maze Runner' should have intuitive instructions and clear output to ensure a good user experience.
2. **Performance:** Maze generation should be efficient and quick, and the game should respond instantly to user inputs.
