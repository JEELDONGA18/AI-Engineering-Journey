create database trustVaultDB;
use trustVaultDB

CREATE TABLE t_users (
    c_user_id INT IDENTITY(1,1) PRIMARY KEY,
    c_full_name NVARCHAR(100) NOT NULL,
    c_email NVARCHAR(100) NOT NULL UNIQUE,
    c_password NVARCHAR(MAX) NOT NULL,
    c_phone NVARCHAR(15),
    c_country NVARCHAR(50),
    c_created_at DATETIME DEFAULT GETDATE()
);

CREATE TABLE t_data_types (
    c_data_id INT IDENTITY(1,1) PRIMARY KEY,
    c_data_name NVARCHAR(100) NOT NULL,
    c_sensitivity_level NVARCHAR(10) NOT NULL CHECK (c_sensitivity_level IN ('Low', 'Medium', 'High'))
);

CREATE TABLE t_partners (
    c_partner_id INT IDENTITY(1,1) PRIMARY KEY,
    c_partner_name NVARCHAR(100) NOT NULL,
    c_is_verified BIT DEFAULT 0,
    c_created_at DATETIME DEFAULT GETDATE()
);

CREATE TABLE t_consents (
    c_consent_id INT IDENTITY(1,1) PRIMARY KEY,
    c_user_id INT NOT NULL,
    c_partner_id INT NOT NULL,
    c_purpose NVARCHAR(MAX) NOT NULL,
    c_start_time DATETIME NOT NULL,
    c_end_time DATETIME NOT NULL,
    c_status NVARCHAR(10) DEFAULT 'Active' CHECK (c_status IN ('Active', 'Revoked', 'Expired')),
    c_created_at DATETIME DEFAULT GETDATE(),

    FOREIGN KEY (c_user_id) REFERENCES t_users(c_user_id) ON DELETE CASCADE,
    FOREIGN KEY (c_partner_id) REFERENCES t_partners(c_partner_id) ON DELETE CASCADE
);

CREATE TABLE t_consent_data (
    c_consent_data_id INT IDENTITY(1,1) PRIMARY KEY,
    c_consent_id INT NOT NULL,
    c_data_id INT NOT NULL,

    FOREIGN KEY (c_consent_id) REFERENCES t_consents(c_consent_id) ON DELETE CASCADE,
    FOREIGN KEY (c_data_id) REFERENCES t_data_types(c_data_id) ON DELETE CASCADE
);

CREATE TABLE t_access_logs (
    c_log_id INT IDENTITY(1,1) PRIMARY KEY,
    c_consent_id INT NOT NULL,
    c_access_time DATETIME DEFAULT GETDATE(),
    c_accessed_by NVARCHAR(100),
    c_ip_address NVARCHAR(45),
    c_location NVARCHAR(100),
    c_notes NVARCHAR(MAX),

    FOREIGN KEY (c_consent_id) REFERENCES t_consents(c_consent_id) ON DELETE CASCADE
);

CREATE TABLE t_documents (
    c_document_id INT IDENTITY(1,1) PRIMARY KEY,
    c_user_id INT NOT NULL,
    c_data_id INT,
    c_document_name NVARCHAR(100) NOT NULL,
    c_file_url NVARCHAR(MAX) NOT NULL,
    c_mime_type NVARCHAR(50),
    c_is_active BIT DEFAULT 1,
    c_uploaded_at DATETIME DEFAULT GETDATE(),

    FOREIGN KEY (c_user_id) REFERENCES t_users(c_user_id) ON DELETE CASCADE,
    FOREIGN KEY (c_data_id) REFERENCES t_data_types(c_data_id) ON DELETE SET NULL
);

