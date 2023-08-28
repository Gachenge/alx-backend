import { error } from "console";
import { validateHeaderName } from "http";
import { createClient, print } from "redis";
import { promisify } from "util"

const client = createClient();

client
.on('connect', () => {
    console.log("Redis client connected to the server");
})
.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

const gets = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName){
    try {
        const value = await gets(schoolName);
        console.log(value);
    } catch (error) {
        console.log(error);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
