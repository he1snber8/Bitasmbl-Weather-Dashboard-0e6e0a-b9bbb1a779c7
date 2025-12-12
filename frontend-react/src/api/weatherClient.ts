const BASE_URL = 'http://localhost:5000/api/weather';

export async function getCurrent(city: string) {
  const res = await fetch(`${BASE_URL}/current?city=${encodeURIComponent(city)}`);
  return res.json();
}
