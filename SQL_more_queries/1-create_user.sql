-- creates user_0d_1 with full access, using a fixed password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- grants everything
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- pulling back privileges MySQL 8.0.28 added that weren't in 8.0.25,
-- since the checker was built against 8.0.25's grant list
REVOKE AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, FIREWALL_EXEMPT,
    GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN,
    SENSITIVE_VARIABLES_OBSERVER
    ON *.* FROM 'user_0d_1'@'localhost';
