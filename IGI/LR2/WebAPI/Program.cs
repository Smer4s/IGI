
using Microsoft.AspNetCore.Http.HttpResults;
using Microsoft.AspNetCore.Mvc;
using MongoDB.Driver;
using WebAPI.Infrastructure;

namespace WebAPI
{
	public class Program
	{
		public static void Main(string[] args)
		{
			var builder = WebApplication.CreateBuilder(args);

			// Add services to the container.

			builder.Services.AddControllers();
			// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
			builder.Services.AddEndpointsApiExplorer();
			builder.Services.AddSwaggerGen();

			builder.Services.AddSingleton<IUsersRepository, UsersRepository>();

			var app = builder.Build();

			// Configure the HTTP request pipeline.
			
				app.UseSwagger();
				app.UseSwaggerUI();
			

			app.UseHttpsRedirection();

			app.UseAuthorization();

			app.MapControllers();

			app.MapGet("/", () => "Goto /swagger/index.html for Api Doc");

			app.Run();
		}
	}
}
