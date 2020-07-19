import discord
import random
import datetime
from operator import itemgetter
from discord.ext import commands

client = commands.Bot(command_prefix='.')
@client.remove_command('help')


@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game('Created by Healer | My prefix is .'))

	print(client.user.name)
	print(client.user.id)
	print('Created By Healer')
	print('____________________')
	
	
@client.event
async def on_message(m):
	con=m.content.lower()
	if con=='hello':
		await m.channel.send(f'{m.author.mention} Hello! How can I help you?')
		
	await client.process_commands(m)
	
@client.command(pass_context=True)
async def love(ctx):
    embed = discord.Embed(title="I Love You :heart:", description="", color=0x0072ff)
    embed.set_footer(text="")
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def loveback(ctx):
    embed = discord.Embed(title="I Love You Too :heart:", description="", color=0x0072ff)
    embed.set_footer(text="")
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def marry(ctx):
    embed = discord.Embed(title="Will You Marry Me? :ring:", description="", color=0x0072ff)
    embed.set_footer(text="")
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(title="{}'s Server Info".format(ctx.message.guild.name), description="Here's What I could Find in Discord's Database!", color=0x0072ff)
    embed.add_field(name="Server Name", value=ctx.message.guild.name)
    embed.add_field(name='Owner',value=ctx.message.guild.owner,inline=True)
    embed.add_field(name="ID", value=ctx.message.guild.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.guild.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.guild.members))
    embed.set_thumbnail(url=ctx.message.guild.icon_url)
    embed.set_footer(text="Moderator bot by HEALER")
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def role(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    embed = discord.Embed(title="Role given", description=f"hey {ctx.author.name}, {user.name} has been giving a role called  {role.name}", color=0x0072ff)
    embed.add_field(name=f"{ctx.author.name}", value='gave the role')
    embed.set_footer(text="Moderator bot by HEALER")
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def rrole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    embed = discord.Embed(title="Role removed", description=f"hey {ctx.author.name}, {user.name} has been removed from a role called  {role.name}", color=0x0072ff)
    embed.add_field(name=f"{ctx.author.name}", value='removed the role')
    embed.set_footer(text="Moderator bot by HEALER")
    await ctx.send(embed=embed)
		
     
@client.command()
async def ping(ctx):
     	await ctx.send(f'pong! {round(client.latency*1000)}ms')
     	
@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=6):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'messages removed')
    
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'Kicked {member.mention}')

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'Banned {member.mention}')
	
@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *,member):
	banned_user = await ctx.guild.bans()
	member_name , member_discriminator = member.split('#')
	for ban_entry in banned_user:
		user = ban_entry.user
		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned the {user.mention}')
			return
	
@client.command()
async def inviteme(ctx):
	await ctx.send(f'https://discord.gg/Ybt8KFn')
	
@client.command()
@commands.has_permissions(administrator=True)
async def log(ctx):
    guild = ctx.guild
    member = ctx.author
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
    }
    channel = await guild.create_text_channel('MOD LOGS', overwrites=overwrites)
	
@client.command()
async def dm(ctx):
    await ctx.author.send("HELLO HOW CAN I HELP YOU? TYPE .help for more commands")

@client.command()
async def secret(ctx):
	if ctx.author.id == 624285851420983296:
		await ctx.author.send("WORKS")

@client.command(name='count')
@commands.has_permissions(administrator=True)
async def calc_stats(ctx, msg_limit=1000, response_size=50):
    async with ctx.message.channel.typing():
        await ctx.send("Starting calculation")
        print("Starting calculation")
        dict_of_reacts = {}
        for channel in ctx.guild.channels:
            if hasattr(channel, 'history'):
                await ctx.send("your channels are: %s" % channel)
                print("your channels are: %s" % channel)
                async for message in channel.history(limit=msg_limit):
                    for reaction in message.reactions:
                        if reaction.custom_emoji:
                            users = await reaction.users().flatten()
                            count = 0
                            for user in users:
                                if not user.bot:
                                    count += 1
                            if count != 0:
                                dict_of_reacts[reaction.emoji.name] = dict_of_reacts.get(reaction.emoji.name, 0) + count

        list_size = 0
        mssage = "the end"
        for emote, count in sorted(dict_of_reacts.items(), key=itemgetter(1), reverse=True):
            mssage += list_msg_format % (emote, count)
            list_size += 1
            if list_size > response_size:
                mssage += "the end"
                await ctx.send(mssage)
                list_size = 0
                mssage = "the end"

        await ctx.send(mssage)
    print("Completed stats calculation!")
	
@client.command()
async def say(ctx, *,content):
	await ctx.send(content)
	
@client.command()
async def invite(ctx):
	await ctx.send(f'https://discord.com/api/oauth2/authorize?client_id=731853060204134400&permissions=8&scope=bot')
	
@client.command()
@commands.has_permissions(administrator=True)
async def ctext(ctx, name):
	await ctx.guild.create_text_channel(name=name)
	
@client.command()
@commands.has_permissions(administrator=True)
async def cvoice(ctx, name):
	await ctx.guild.create_voice_channel(name=name)
	
@client.command()
@commands.has_permissions(administrator=True)
async def delc(ctx):
 c = await client.fetch_channel(ctx.channel.id)
 await c.delete()

 
@client.command()
async def av(ctx, *, member: discord.Member=None):
    if not member: 
        member = ctx.message.author 
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)
	
@client.command()
async def owner(ctx, member):
	await ctx.send(f'ownership has been given to user')
			
@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member : discord.Member):
	guild = ctx.guild
	for role in guild.roles:
		if role.name=="Muted":
			await member.remove_roles(role)
			await ctx.send("{} has {} been unmuted" .format (member.mention,ctx.author.mention))
			return
			

@client.command(pass_context = True)     
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x0072ff)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)
    
@client.command(pass_context = True) 
async def info(ctx):
    embed = discord.Embed(title="{}'s info".format(client.user.name), description="Here's my ID card.", color=0x0072ff)
    embed.add_field(name="Name", value=client.user.name, inline=True)
    embed.add_field(name="ID", value=client.user.id, inline=True)
    embed.add_field(name="Language", value="Python")
    embed.add_field(name="Owner", value="Healer")
    await ctx.send(embed=embed)
    

@client.command()
async def help(ctx):
	embed=discord.Embed(title='MODERATOR',description='My prefix is .', color=0x0072ff)
	embed.add_field(name='invite',value='sends bot invite link')
	embed.add_field(name='inviteme', value='Invites user to server')
	embed.add_field(name='say', value='says your message')
	embed.add_field(name='ping', value='shows user latency')
	embed.add_field(name='av', value='shows avatar')
	embed.add_field(name='choose', value='choose between options')
	embed.add_field(name='userinfo', value='gives info about mentioned user')
	embed.add_field(name='add', value='to add some numbers')
	embed.add_field(name='sub', value='to subtract some numbers')
	embed.add_field(name='mul', value='to multiply some numbers')
	embed.add_field(name='div', value='to divide some numbers')
	embed.add_field(name='cool', value='to see a user is cool or not')
	embed.add_field(name='dm', value='the bot will send a DM message')
	embed.add_field(name='love', value='the bot will say I love you')
	embed.add_field(name='loveback', value='the bot will say I love you too')
	embed.add_field(name='marry', value='the bot will say to marry you')
	embed.add_field(name='serverinfo', value='to see server info')
	embed.add_field(name='adhelp', value='to see admins only commands')
	await ctx.send(embed=embed)
	
	
@client.command()
@commands.has_permissions(administrator=True)
async def adhelp(ctx):
	embed=discord.Embed(title='Admins only',description='commands for Admins only', color=0x0072ff)
	embed.add_field(name='clear', value='to clear messages')
	embed.add_field(name='cvoice', value='create voice channel')
	embed.add_field(name='ctext', value='create text channel')
	embed.add_field(name='delc', value='deletes a channel stay in the channel to do it (text only)')
	embed.add_field(name='kick', value='to kick a user')
	embed.add_field(name='ban', value='to ban a user')
	embed.add_field(name='unban', value='to unban a user')
	embed.add_field(name='unmute', value='to unmute a user')
	embed.add_field(name='count', value='to count all channels of a server')
	embed.add_field(name='role', value='to give user a role')
	embed.add_field(name='rrole', value='to remove user from a role')
	embed.add_field(name='log', value='to create a log channel')
	
	await ctx.send(embed=embed)
	

        
@client.command()
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))
        
@client.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)
        
@client.command()
async def sub(ctx, left: int, right: int):
    await ctx.send(left - right)
    
@client.command()
async def mul(ctx, left: int, right: int):
    await ctx.send(left * right)
    
@client.command()
async def div(ctx, left: int, right: int):
    await ctx.send(left / right)
    
@client.command()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is cool'.format(ctx))

@client.command(name='bot')
async def bot(ctx):
    await ctx.send('Yes, the bot is cool.')
    
        

        
        
client.run('NzM0Mjg0NzY0MTQ3NzQ0ODQ5.XxPkKw.hVlVNfQdzkhmoHZ5ghdtG-faoj0')
