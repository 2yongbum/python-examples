import asyncio
import pexpect

p = pexpect.spawn('python')
p.setecho(False)
p.waitnoecho()
b = pexpect.spawn('bash')
b.setecho(False)
b.waitnoecho()

p.expect_exact('>>> ')
b.expect_exact("$ ")

p.sendline("import time; time.sleep(4); print('done')")
b.sendline("sleep 2 && echo 'done'")

async def wait_python():
    await p.expect('done', async_=True)
    print("Python done")

async def wait_bash():
    await b.expect('done', async_=True)
    print("Bash done")

async def main():
    await asyncio.gather(wait_python(), wait_bash())

asyncio.run(main())
