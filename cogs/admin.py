import asyncio
from discord.ext import commands

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def complete(self, ctx, message: str):
        await ctx.send(message)
        await asyncio.sleep(0.5)
        await ctx.message.delete()

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def sync_commands(self, ctx):
        await self.bot.tree.sync()
        await AdminCog.complete(self, ctx, '/commands synced')

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def load(self, ctx, extension: str):
        await self.bot.load_extension(f'cogs.{extension}')
        await AdminCog.complete(self, ctx, f'Loaded: {extension}')

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def unload(self, ctx, extension: str):
        await self.bot.unload_extension(f'cogs.{extension}')
        await AdminCog.complete(self, ctx, f'Unloaded: {extension}')

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def reload(self, ctx, extension: str):
        await self.bot.unload_extension(f'cogs.{extension}')
        await AdminCog.complete(self, ctx, f'Reloaded: {extension}')

async def setup(bot):
    await bot.add_cog(AdminCog(bot))
