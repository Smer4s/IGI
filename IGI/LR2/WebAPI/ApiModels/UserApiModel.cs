using MongoDB.Bson;

namespace WebAPI.ApiModels
{
	public class UserApiModel
	{
		public ObjectId Id { get; set; }
		public string Name { get; set; } = null!;
		public string Email { get; set; } = null!;
	}
}
