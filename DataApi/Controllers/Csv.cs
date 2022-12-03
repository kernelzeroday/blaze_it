//controller for the csv file

using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace DataApi.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class Csv : ControllerBase
    {
        private readonly ILogger<Csv> _logger;

        public Csv(ILogger<Csv> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public IEnumerable<Csv> Get()
        {
            var rng = new Random();
            return Enumerable.Range(1, 5).Select(index => new Csv
            {
                Date = DateTime.Now.AddDays(index),
                TemperatureC = rng.Next(-20, 55),
                Summary = Summaries[rng.Next(Summaries.Length)]
            })
            .ToArray();
        }
    }
}


