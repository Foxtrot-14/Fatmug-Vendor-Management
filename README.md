# Fatmug-Vendor-Management-API

This API allows you to manage vendors and their historical performance records.

## Endpoints

### Get Vendors

- **URL:** `/api/vendors/`
- **Method:** GET
- **Description:** Retrieve a list of all vendors.
- **Response:** Returns a list of vendors with their details.

### Add Vendor

- **URL:** `/api/vendors/`
- **Method:** POST
- **Description:** Add a new vendor.
- **Request Body:**
```json
  {
  "name": "Example Vendor",
  "contact_details": "example@example.com",
  "address": "123 Example St, Example City",
  "vendor_code": "EX123"
  }
```
- **Response:** Returns the details of the newly added vendor if successful.

### Get Vendor by ID

- **URL:** `/api/vendors/<int:vendor_id>/`
- **Method:** GET
- **Description:** Retrieve details of a specific vendor by its ID.
- **Response:** Returns the details of the specified vendor.

### Update Vendor

- **URL:** `/api/vendors/<int:vendor_id>/`
- **Method:** PUT
- **Description:** Update an existing vendor's details.
- **Request Body:** 
```json
{
  "name": "Updated Vendor Name",
  "contact_details": "updated@example.com",
  "address": "456 Updated St, Updated City",
  "vendor_code": "UPD456"
}
```
- **Response:** Returns the details of the updated vendor if successful.

### Delete Vendor

- **URL:** `/api/vendors/<int:vendor_id>/`
- **Method:** DELETE
- **Description:** Delete an existing vendor.
- **Response:** Returns a success message if the vendor is deleted successfully.

### Get Purchase Orders

- **URL:** `/api/purchase_orders/`
- **Method:** GET
- **Description:** Retrieve a list of all Purchase Order.
- **Response:** Returns a list of Purchase Order with their details.

### Add Purchase Orders

- **URL:** `/api/purchase_orders/`
- **Method:** POST
- **Description:** Add a new vendor.
- **Request Body:**
```json
{
  "po_number": "PO123",
  "vendor": 1,
  "order_date": "2024-05-07T08:00:00Z",
  "delivery_date": "2024-05-14T08:00:00Z",
  "items": [
    {"name": "Item 1", "quantity": 10},
    {"name": "Item 2", "quantity": 20}
  ],
  "quantity": 2,
  "status": "pending",
  "issue_date": "2024-05-07T08:00:00Z"
}

```
- **Response:** Returns the details of the newly added Purchase Order if successful.

### Get Purchase Orders by ID

- **URL:** `/api/purchase_orders/<int:po_id>/`
- **Method:** GET
- **Description:** Retrieve details of a specific Purchase Order by its ID.
- **Response:** Returns the details of the specified Purchase Order.

### Update Purchase Orders

- **URL:** `/api/purchase_orders/<int:po_id>/`
- **Method:** PUT
- **Description:** Update an existing Purchase Order's details.
- **Request Body:** 
```json
{
  "po_number": "PO123",
  "vendor": 1,
  "order_date": "2024-05-07T08:00:00Z",
  "delivery_date": "2024-05-14T08:00:00Z",
  "items": [
    {"name": "Item 1", "quantity": 10},
    {"name": "Item 2", "quantity": 20}
  ],
  "quantity": 2,
  "status": "completed",
  "issue_date": "2024-05-07T08:00:00Z"
}
```
- **Response:** Returns the details of the updated Purchase Order if successful.

### Delete Purchase Orders

- **URL:** `/api/purchase_orders/<int:po_id>/`
- **Method:** DELETE
- **Description:** Delete an existing Purchase Order.
- **Response:** Returns a success message if the Purchase Order is deleted successfully.

### Get Historical Performance

- **URL:** `/api/vendors/<int:vendor_id>/performance`
- **Method:** GET
- **Description:** Retrieve historical performance records for all vendors.
- **Response:** Returns a list of historical performance records for all vendors.

## Authentication

- Use token-based authentication to authenticate requests.
