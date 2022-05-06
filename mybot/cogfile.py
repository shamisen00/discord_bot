from discord.ext import commands
import discord

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name='on_message')
    async def good_reaction(self, message):
        if message.author.bot:
            return
        if 'いいね' in message.content:
            await message.add_reaction('\U0001f44d')
    
    @commands.Cog.listener(name='on_message')
    async def good_reaction(self, message):
        if self.bot.user in message.mentions and "^^" in message.content:
            await message.channel.send(file=discord.File("data/test.png"))
    
    @commands.command()
    async def test(self, ctx, arg):
        await ctx.send(arg)

def setup(bot):
    bot.add_cog(MyCog(bot))