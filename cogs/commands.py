from discord.ext import commands

class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello!')

async def setup(bot):
    await bot.commands(events(bot))
