from discord.ext import commands

class CommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello!')

async def setup(bot):
    await bot.commands(CommandsCog(bot))
