namespace WebAPI.Infrastructure
{
	public interface IUsersRepository
	{
		public Task<IEnumerable<User>> GetUsers();
		public Task<User> GetUser(string id);
		public Task AddUser(User user);
		public Task DeleteUser(string id);
		public Task UpdateUser(User user);
	}
}
