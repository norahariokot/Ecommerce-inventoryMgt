// Purchase order
console.log(productList)

// Function to add form fields to the purchase order form, its triggered by add(row) btn and its children
    let formInputs = document.querySelector('.form-inputs');
        let clonedNode = formInputs.cloneNode(true);document.addEventListener('DOMContentLoaded', function() {
    // Your code here, including the selection and event listener setup
    function add_item(event) {
        // The following function is used to prevent the default behaviour of button submission which refreshes a page whenever btn within a form is clicked
        event.preventDefault();
        // Clone the form-inputs div 
    
        // Update IDs to make them unique
        let inputs = clonedNode.querySelectorAll('input');
        for (let i = 0; i < inputs.length; i++) {
                inputs[i].id = inputs[i].id + i;
        }
    
        // Append the new form to the body or any other desired location
        const divContainer = document.querySelector(".form-details")
        divContainer.appendChild(clonedNode);
        }
    
    // Get references to the select and input elements
    let selected = document.querySelector('#PO_item');
    let inputElement = document.querySelector('#PO_specs');
    let inputprice = document.querySelector('#PO_px');
    
    
    // Add an event listener to the select element
    selected.addEventListener('change', function() {
        // Update the value of the input field based on the selected option
        const selectedValue = selected.value;
    
        // To send the selected value to the Flask web server:
        // Define a fetch function and evoke it using the window.onload event
        function sendFetchRequest(selected) {
            fetch("/purchaseorder_info", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ selected: selected }),
            })
            .then(response => response.json())
            .then(data => {
                // handle POST response if necessary
                return fetch('/get_info');
            })
            .then(response => response.json())
            .then(data => {
                // handle GET response
                console.log(data);
                // Update your HTML or perform other actions with the received data
            })
            .catch(error => console.error('Error:', error));
        }
    
        // Call the function with the selected value
        sendFetchRequest(selectedValue);
    });
    
});


console.log(categoryDict);

// Function to update subcategories based on the selected category in Form 1
function updateSubcategories() {
    const categorySelect = document.getElementById('categoryForm1');
    const subcategorySelect = document.getElementById('subcategoryForm1');

    // Clear existing subcategories
    subcategorySelect.innerHTML = '<option value="" selected disabled>Select a subcategory</option>';

    // Get the selected category
    const selectedCategory = categorySelect.value;

    // Populate subcategories based on the selected category
    categoryDict[selectedCategory].forEach(subcategory => {
        const option = document.createElement('option');
        option.value = subcategory;
        option.text = subcategory;
        subcategorySelect.add(option);
    });
}

// Populate categories in the category select
const categorySelect = document.getElementById('categoryForm1');
Object.keys(categoryDict).forEach(category => {
    const option = document.createElement('option');
    option.value = category;
    option.text = category;
    categorySelect.add(option);
});

// Function to update subcategories based on the selected category in Form2
function updateSubcategories2() {
    const categorySelect2 = document.getElementById('categoryForm2');
    const subcategorySelect2 = document.getElementById('subcategoryForm2');

    // Clear existing subcategories
    subcategorySelect2.innerHTML = '<option value="" selected disabled>Select a subcategory</option>';

    // Get the selected category
    const selectedCategory2 = categorySelect2.value;

    // Populate subcategories based on the selected category
    categoryDict[selectedCategory2].forEach(subcategory => {
        const option2 = document.createElement('option');
        option2.value = subcategory;
        option2.text = subcategory;
        subcategorySelect2.add(option2);
    });
}

// Function to add the suppliers categories to the add suppliers form
function addSupplierCategory() {
    event.preventDefault(); // Prevent default form submission behavior

    // Clone the existing div with its contents
    var originalDiv = document.querySelector('.supplier-categories');
    var cloneDiv = originalDiv.cloneNode(true);
    
    // Insert the cloned div after the last cloned div, or after the original div if there are no clones yet
    var lastClone = document.querySelector('.supplier-categories:last-of-type');
    if (lastClone) {
        lastClone.parentNode.insertBefore(cloneDiv, lastClone.nextSibling);
    } else {
        originalDiv.parentNode.insertBefore(cloneDiv, originalDiv.nextSibling);
    }
}

