CREATE TYPE trips_request_device_enum AS ENUM (
    'android',
    'iphone',
    'sms',
    'mobile_web'
);


CREATE TYPE trips_status_enum AS ENUM(
    'completed',
    'cancelled_by_driver',
    'cancelled_by_client'
);

CREATE TYPE users_role_enum AS ENUM(
    'client',
    'driver',
    'partner'
);

CREATE TABLE trips (
    id integer NOT NULL,
    client_id integer NOT NULL,
    driver_id integer,
    client_rating integer,
    driver_rating integer,
    request_device trips_request_device_enum,
    status trips_status_enum,
    predicted_eta integer,
    actual_eta integer,
    city_id integer DEFAULT 1 NOT NULL,
    request_at timestamp with time zone
);

CREATE TABLE users (
    usersid integer NOT NULL,
    email character varying(100),
    firstname character varying(45),
    lastname character varying(45),
    banned boolean DEFAULT false,
    role users_role_enum,
    creationtime timestamp with time zone
);
