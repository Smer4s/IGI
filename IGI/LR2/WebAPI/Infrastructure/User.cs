using MongoDB.Bson;

namespace WebAPI.Infrastructure
{
	public class User
	{
		public ObjectId Id { get; set; }
		public string Name { get; set; } = null!;
		public string Email { get; set; } = null!;
		public string Password { get; set; } = null!;
	}
}
