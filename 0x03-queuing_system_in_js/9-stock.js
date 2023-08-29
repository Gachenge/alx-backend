import { createClient } from 'redis';
import { promisify } from 'util';

const express = require('express');

const app = express();

const port = 1245;

const client = createClient();
const getAsync = promisify(client.get).bind(client);


const listProducts = [
    {itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4},
    {itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10},
    {itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2},
    {itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5}
]

function getItemById(id) {
    return(listProducts.filter((item) => item.itemId === id)[0]);
}

function reserveStockById(itemId, stock) {
    client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
    return(await getAsync(`item.${itemId}`));
}

app.get('/list_products', (req, res) => {
    res.json(listProducts);
})

app.get('/list_products/:itemId', async(req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);
    if (!item) {
        res.json({"status": "Product not found"});
        return;
    }
    const product = await getCurrentReservedStockById(itemId);
    if (!product){
        await reserveStockById(itemId, item.initialAvailableQuantity);
        item.quantity = item.initialAvailableQuantity;
    }
    else {
        item.quantity = product;
    }
    res.json(item)
})

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);
    if (!item) {
        res.json({"status":"Product not found"});
        return;
    }
    let stock = await getCurrentReservedStockById(itemId);
    if (stock === null) {
        stock = item.initialAvailableQuantity;
    }
    if (stock <= 0) {
        res.json({"status": "Not enough stock available", "itemId": `${itemId}`})
    }
    else {
        reserveStockById(itemId, Number(stock) - 1);
        res.json({"status": "Reservation confirmed", "itemId": `${itemId}`})
    }
})

app.listen(port);
