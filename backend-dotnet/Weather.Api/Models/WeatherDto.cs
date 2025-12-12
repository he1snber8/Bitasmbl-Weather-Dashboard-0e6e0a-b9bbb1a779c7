namespace Weather.Api.Models;

public class WeatherDto
{
    public string City { get; set; } = string.Empty;
    public DateTime Timestamp { get; set; }
    public double Temperature { get; set; }
}
