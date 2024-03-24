using Microsoft.AspNetCore.Mvc;
using WebAPI.ApiModels;
using WebAPI.Infrastructure;

namespace WebAPI.Controllers
{
	[Route("/api/[controller]")]
	[ApiController]
	public class UsersController(IUsersRepository usersRepository) : ControllerBase
	{
		[HttpGet]
		public async Task<IActionResult> GetUsers()
		{
			var list = await usersRepository.GetUsers();

			var result = list.Select(x => new UserApiModel()
			{
				Id = x.Id,
				Name = x.Name,
				Email = x.Email,
			});

			return Ok(result);
		}

		[HttpGet("{id}")]
		public async Task<IActionResult> GetUser([FromRoute] string id)
		{
			var user = await usersRepository.GetUser(id);

			var apiUser = new UserApiModel()
			{
				Id = user.Id,
				Name = user.Name,
				Email = user.Email
			};

			return Ok(apiUser);
		}

		[HttpPost]
		public async Task<IActionResult> PostUser(User apiUser)
		{
			await usersRepository.AddUser(apiUser);

			return Ok();
		}

		[HttpPut]
		public async Task<IActionResult> UpdateUser(User apiUser)
		{
			await usersRepository.UpdateUser(apiUser);

			return Ok();
		}

		[HttpDelete("{id}")]
		public async Task<IActionResult> DeleteUser([FromRoute] string id)
		{
			await usersRepository.DeleteUser(id);

			return Ok();
		}
	}
}
