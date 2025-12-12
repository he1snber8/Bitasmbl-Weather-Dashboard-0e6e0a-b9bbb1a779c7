# Bitasmbl-Weather-Dashboard-0e6e0a-b9bbb1a779c7

## Description
Build a web application that displays current weather, multi-day forecasts, and visualizes trends with charts. The project focuses on integrating APIs, dynamic front-end updates, and data visualization for an interactive user experience.

## Tech Stack
- FastAPI
- ASP.NET Core
- React

## Requirements
- Fetch real-time weather data from a public API
- Display multi-day weather forecasts with clear UI elements
- Visualize temperature, humidity, or other metrics with charts
- Support user interactions, such as searching by city
- Optionally cache API responses to improve performance

## Installation
bash
git clone https://github.com/he1snber8/Bitasmbl-Weather-Dashboard-0e6e0a-b9bbb1a779c7.git
cd Bitasmbl-Weather-Dashboard-0e6e0a-b9bbb1a779c7


### React
bash
npm install


### FastAPI
bash
pip install -r requirements.txt


### ASP.NET Core
bash
dotnet restore


## Usage
### React
bash
npm start


### FastAPI
bash
uvicorn main:app --reload


### ASP.NET Core
bash
dotnet run


## Implementation Steps
1. Set up React app for UI, search by city, and display of current weather and multi-day forecasts.
2. Implement charts in React to visualize temperature, humidity, or other metrics.
3. Create FastAPI service to fetch real-time weather data from a public API.
4. Create ASP.NET Core service as an additional backend layer for handling weather-related requests.
5. Integrate React with FastAPI and/or ASP.NET Core for dynamic front-end updates.
6. Optionally add caching of API responses in the backend to improve performance.

## API Endpoints
- Endpoint(s) to fetch real-time weather data from a public API via backend
- Endpoint(s) to provide multi-day forecasts to the React front-end