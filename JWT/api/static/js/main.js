let file = new FormData();
let dropArea = document.getElementById('dragArea');
let preview = document.getElementById('preview');
let info = document.querySelector('.info');
let result = document.getElementById('resultArea-resultText');
let resultArea = document.getElementById('result');
const reader = new FileReader();
const fileByteArray = [];

const selectFileOnClick = () => {
    let input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
    input.onchange = e => {
        if (e.target.files.length > 0) {
            file = new FormData();
            file.append("img", e.target.files[0]);
            viewPreviewImg();
            reader.readAsArrayBuffer(e.target.files[0]);
            reader.onloadend = (evt) => {
                if (evt.target.readyState === FileReader.DONE) {
                    const arrayBuffer = evt.target.result,
                        array = new Uint8Array(arrayBuffer);
                    for (const a of array) {
                        fileByteArray.push(a);
                    }
                }
            }
            input.remove();
        }
    }
    input.click();

}

const viewPreviewImg = () => {
    let reader = new FileReader();
    reader.onloadend = function() {
        preview.src = reader.result;
    }
    if (file) {
        reader.readAsDataURL(file.get("img"));
        preview.classList.remove('hidden');
        info.classList.add('hidden');
    } else {
        preview.src = "";
        preview.classList.add('hidden');
        info.classList.remove('hidden');
    }
}

dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dragArea.classList.add("dragArea__highlight");
});

["dragleave", "dragend"].forEach((type) => {
    dropArea.addEventListener(type, (e) => {
        dropArea.classList.remove("dragArea__highlight");
    });
});

dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    if (e.dataTransfer.files.length > 0) {
        let files = [...e.dataTransfer.files];
        file = new FormData();
        file.append("img", files[0]);
        reader.readAsArrayBuffer(files[0]);
        reader.onloadend = (evt) => {
            if (evt.target.readyState === FileReader.DONE) {
                const arrayBuffer = evt.target.result,
                    array = new Uint8Array(arrayBuffer);
                for (const a of array) {
                    fileByteArray.push(a);
                }
            }
        }
        viewPreviewImg();
    }
    dropArea.classList.remove("dragArea__highlight");
});


const fetchData = async () => {
    if (file.get("img") !== null) {
        const response = await fetch("http://localhost:8000/api/v2/file", {
            method: 'POST',
            mode: 'cors',
            cache: 'no-cache',
            headers: {
                'Content-Type': 'undefined'
            },
            body: JSON.stringify({
                "img": fileByteArray
            })
        });
        if ((await response.text()).length > 0) {
            result.innerHTML = response.text();
            resultArea.classList.remove('hidden');
        }
    } else {
        alert("Сначала выберите файл для обработки");
    }
}