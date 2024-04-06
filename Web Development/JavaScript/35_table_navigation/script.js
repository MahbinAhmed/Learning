let table = document.body.firstElementChild.nextElementSibling;
// console.log(table);
console.log(table.rows);
console.log(table.caption);
console.log(table.tHead);
console.log(table.tFoot);
console.log(table.tBodies);

let table_body = table.children[1];
console.log(table.children[1].rows);

console.log(table.rows[1].cells);
console.log(table.rows[3].rowIndex);
console.log(table.rows[1].children);
console.log(table.rows[0].children[1].cellIndex);
console.log(table.rows[3].sectionRowIndex);