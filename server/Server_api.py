import uvicorn
from fastapi import FastAPI
from selenium.webdriver import Keys
from selenium_driverless import webdriver
from selenium_driverless.types.by import By

app = FastAPI()


async def srch(job_name,region):
    options = webdriver.ChromeOptions()
    async with (webdriver.Chrome(options=options) as driver):
        await driver.get('https://www.jobs.cz/', wait_load=True)
        await driver.sleep(1)
        #await driver.wait_for_cdp("Page.domContentEventFired", timeout=15)

        # wait 10s for elem to exist
        elem = await driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div/div[2]/button[2]', timeout=10)
        await elem.click(move_to=True)
        await driver.sleep(1)
        text_box = await driver.find_element(By.XPATH, "//div[@id='hp-search-box']/form/div/div/div/div")
        await text_box.send_keys(job_name)
        print(text_box)
        text_box2 = await driver.find_element(By.XPATH, "/html/body/section/div/div/form/div[2]/div/div/div[1]")
        await text_box2.send_keys(region)
        print(text_box2)
        hledat = await driver.find_element(By.XPATH,"/html/body/section/div/div/form/button", timeout=10)
        await hledat.click(move_to=True)
        await driver.sleep(5)

async def prace(job_name,region):
    options = webdriver.ChromeOptions()
    async with (webdriver.Chrome(options=options) as driver):
        await driver.get('https://www.prace.cz/', wait_load=True)
        await driver.sleep(1)
    elem = await driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div/div[2]/button[2]", timeout=10)
    await elem.click(move_to=True)
    await driver.sleep(1)
    text_box = await driver.find_element(By.XPATH, "/html/body/div[3]/form/div/div[1]/div[3]/div/ul")
    await text_box.send_keys(job_name)
    print(text_box)
    text_box2 = await driver.find_element(By.XPATH, "/html/body/div[3]/form/div/div[1]/div[2]/div/ul")
    await text_box2.send_keys(region)
    print(text_box2)
    hledat = await driver.find_element(By.XPATH, "/html/body/div[3]/form/div/div[2]/div/div/button", timeout=10)
    await hledat.click(move_to=True)
    await driver.sleep(10)


@app.get("/jobs/")
async def read_job_region(job:str,region:str):
    await srch(job, region)
    await prace(job, region)
    return {"job": job, "region": region}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)