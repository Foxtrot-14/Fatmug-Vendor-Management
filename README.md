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
- **Request Body:** JSON object containing details of the vendor to be added (name, contact details, address, vendor code).
- **Response:** Returns the details of the newly added vendor if successful.

### Get Historical Performance

- **URL:** `/api/historical-performance/`
- **Method:** GET
- **Description:** Retrieve historical performance records for all vendors.
- **Response:** Returns a list of historical performance records for all vendors.

### Add Historical Performance

- **URL:** `/api/historical-performance/`
- **Method:** POST
- **Description:** Add a new historical performance record for a vendor.
- **Request Body:** JSON object containing details of the historical performance record (vendor ID, date, on-time delivery rate, quality rating average, average response time, fulfillment rate).
- **Response:** Returns the details of the newly added historical performance record if successful.

### Update Vendor

- **URL:** `/api/vendors/<vendor_id>/`
- **Method:** PUT, PATCH
- **Description:** Update an existing vendor's details.
- **Request Body:** JSON object containing the updated details of the vendor.
- **Response:** Returns the details of the updated vendor if successful.

### Delete Vendor

- **URL:** `/api/vendors/<vendor_id>/`
- **Method:** DELETE
- **Description:** Delete an existing vendor.
- **Response:** Returns a success message if the vendor is deleted successfully.

### Get Vendor by ID

- **URL:** `/api/vendors/<vendor_id>/`
- **Method:** GET
- **Description:** Retrieve details of a specific vendor by its ID.
- **Response:** Returns the details of the specified vendor.

### Add Performance for Vendor

- **URL:** `/api/vendors/<vendor_id>/add-performance/`
- **Method:** POST
- **Description:** Add historical performance records for a specific vendor.
- **Request Body:** JSON object containing details of the historical performance record (date, on-time delivery rate, quality rating average, average response time, fulfillment rate).
- **Response:** Returns the details of the newly added historical performance record if successful.

## Authentication

- Authentication is required for certain endpoints (e.g., add/update/delete vendor).
- Use token-based authentication (e.g., JWT) to authenticate requests.
