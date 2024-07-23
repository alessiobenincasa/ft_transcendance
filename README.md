# ft_transcendance

FT\_Transcendence
=========================

A comprehensive web application project focused on enhancing gaming experiences through innovative features, security, and data-driven elements.

Table of Contents
-----------------

* [Project Overview](#project-overview)
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

Project Overview
----------------

FT\_Transcendence is a web application project that offers a variety of gaming experiences, user authentication, and cybersecurity measures. The project is designed to provide users with a secure, engaging, and customizable gaming platform.

Features
--------

### Authentication System

* Secure user sign-in with authentication tokens and user information exchange.
* User-friendly login and authorization flows adhering to best practices and security standards.

### Gameplay and User Experience

* Remote players: Play with distant players on separate computers.
* Multiple players: Support for more than two players with live control.
* New game with user history and matchmaking: Introduce a new game, track user gameplay statistics, and facilitate matchmaking.
* Game customization options: Offer power-ups, attacks, different maps, and other customization features for all games.
* Live chat: Send direct messages, block users, invite users to play, receive tournament notifications, and access other players' profiles.

### AI-Algo

* AI opponent: Introduce an AI player that provides a challenging and engaging gameplay experience without relying on the A\* algorithm.
* User and game stats dashboards: Display user and game session statistics through user-friendly dashboards.

### Cybersecurity

* WAF/ModSecurity with hardened configuration and HashiCorp Vault for secrets management: Enhance security infrastructure with robust protection measures.
* GDPR compliance options: Enable user anonymization, local data management, and account deletion.
* Two-factor authentication (2FA) and JSON Web Tokens (JWT): Strengthen user account security and enhance authentication and authorization.

### DevOps

* Infrastructure setup with ELK (Elasticsearch, Logstash, Kibana) for log management: Establish a powerful log management and analysis system.
* Monitoring system: Set up a comprehensive monitoring system using Prometheus and Grafana.
* Designing the backend as microservices: Enhance the system's architecture with a microservices design approach.

Installation
------------

1. Clone the repository:
```bash
git clone https://github.com/your-username/ft_transcendence_surprise.git
```
1. Install dependencies:
```bash
cd ft_transcendence
npm install
```
1. Configure environment variables:
```bash
cp .env.example .env
```
Edit the `.env` file to include your specific configuration.

1. Build and run the project:
```bash
npm run build
npm start
```
Usage
-----

Access the web application at `http://localhost:3000` and explore the various features and games.

Contributing
------------

Contributions are welcome! Please submit a pull request with your proposed changes. Make sure to include relevant documentation and test cases.

License
-------

This project is licensed under the [MIT License](LICENSE).

Contact
-------

For any questions or inquiries, please contact alben2992@outlook.fr
