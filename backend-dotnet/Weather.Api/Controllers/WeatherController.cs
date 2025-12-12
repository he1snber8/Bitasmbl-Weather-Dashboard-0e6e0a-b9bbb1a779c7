using Microsoft.AspNetCore.Mvc;
using Weather.Api.Models;

[ApiController]
[Route("api/[controller]")]
public class WeatherController : ControllerBase
{
    [HttpGet("current")] public ActionResult<WeatherDto> GetCurrent(string city)=>Ok();
}
