// Використовуємо платформу NodeJS "Запускаємо проект"
// Імпортуємо "readline" замість використання методу prompt, тому що ми використовуємо платформу NodeJS
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const DATA = [
    {id: 1, name: 'асус', guaranteeByYear: 12, price: 12000},
    {id: 2, name: 'холодильник', guaranteeByYear: 3, price: 2000},
    {id: 3, name: 'телевізор', guaranteeByYear: 2, price: 5000},
    {id: 4, name: 'чайник', guaranteeByYear: 6, price: 32000},
];

var sumProdTovary = 0;

var dataLength = DATA.length;

var istoriaProdajy = [];

// Створення нового товару
function createNewDATA(id, name, guarantee, price) {
    let createNewDATA = {
        "id": id,
        "name": name, 
        "guaranteeByYear": guarantee,
        "price": price
    };
    DATA.push(createNewDATA);
};

function addProdaz(time , name , price) {
    let addProdaz = {
        "time": time,
        "name": name, 
        "price": price
    };
    istoriaProdajy.push(addProdaz);
};

function request(DATA){
    try {
    // Запит
    rl.question("Бажаєте знайти техніку, видалити або додати? ( info || add || exit || remove || sell ): ", (text) => {
        if(text === 'add'){
            console.log('-'.repeat(20));
            rl.question("Id: ", (id) => {
                rl.question("name: ", (name) => {
                    rl.question("guarantee: ", (guarantee) => {
                        rl.question("price: ", (price) => {
                            createNewDATA(id, name, guarantee, price);
                            console.log('-'.repeat(20));
                            console.log(`Успішно добавленно!`);
                            request(DATA);
                        })
                    })
                })
            });
        } 
        // Пошук товару
        else if(text === "info"){
            try {
                rl.question("Назва товару: ", (text) => {
                    DATA.forEach(element => {
                        if(element.name === text){
                            console.log('-'.repeat(50));
                            console.log('Товар знайдено..','\n',element);
                            console.log('-'.repeat(50));
                            request(DATA);
                        }
                    });
                    request(DATA);
                });
            } catch (e) {
                console.log('Помилка!', e.message);
                request(DATA);
            }
        }
        // Видалення товару
        else if(text === "remove"){
            rl.question('Назва товару для виделленя: ', (rmText) => {
                var removeIndex = DATA.map(function(item) {return item.name}).indexOf(rmText);
                DATA.splice(removeIndex, 1)
                console.log('-'.repeat(20));
                console.log('Успішно видалено!');
                console.log('-'.repeat(20));
                request(DATA);
            })
        }

        // Продаж товару
        else if(text === 'sell') {
            rl.question('Товар для продажі: ', (text) => {
                DATA.forEach(element => {
                    if(element.name === text){
                        sumProdTovary += +element.price;
                        let time = new Date().toTimeString().split(' ');
                        let date = new Date().toJSON().split('T');
                        let fullTime = time[0] + ' ' + date[0];
                        addProdaz(fullTime, element.name, element.price);
                        console.log('-'.repeat(20));
                        console.log('Товар було продано..');
                        console.log('Сумма в касі:', sumProdTovary);
                        console.log('-'.repeat(20));
                        request(DATA);
                    }
                });
                request(DATA);
            })
        }
        
        // Інформація продажів
        else if(text === 'infoAboutSells') {
            istoriaProdajy.forEach(tovar => {
                console.log(tovar);
            })
            request(DATA);
        }
        else if(text === 'exit'){
            console.log("Exit..");
            process.exit();
        }else {
            console.log("Введіть коректну команду..");
            request(DATA);
        };
    });
    } catch (e) {
        console.log("Щось сталось.. \n",  e.message);
        request(DATA);
    };
};

// start
request(DATA);