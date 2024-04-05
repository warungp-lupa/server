-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.

DROP DATABASE IF EXISTS palupi;
CREATE DATABASE palupi;

BEGIN;


CREATE TABLE IF NOT EXISTS public.menu
(
    id_menu integer NOT NULL DEFAULT nextval('menu_id_menu_seq'::regclass),
    nama character varying(100) COLLATE pg_catalog."default" NOT NULL,
    harga integer,
    kuantitas integer,
    deskripsi character varying COLLATE pg_catalog."default",
    CONSTRAINT menu_pkey PRIMARY KEY (id_menu)
);

CREATE TABLE IF NOT EXISTS public.pembayaran
(
    id_pembayaran integer NOT NULL DEFAULT nextval('pembayaran_id_pembayaran_seq'::regclass),
    id_pembeli integer,
    opsi_bayar character varying(20) COLLATE pg_catalog."default",
    total_harga integer,
    CONSTRAINT pembayaran_pkey PRIMARY KEY (id_pembayaran)
);

CREATE TABLE IF NOT EXISTS public.pemesanan
(
    id_pembeli integer NOT NULL DEFAULT nextval('pemesanan_id_pembeli_seq'::regclass),
    nama character varying(50) COLLATE pg_catalog."default",
    alamat character varying(50) COLLATE pg_catalog."default",
    telp character varying(15) COLLATE pg_catalog."default",
    pesan character varying(50) COLLATE pg_catalog."default",
    makanditempat boolean,
    CONSTRAINT pemesanan_pkey PRIMARY KEY (id_pembeli)
);

CREATE TABLE IF NOT EXISTS public."user"
(
    id_user integer NOT NULL DEFAULT nextval('user_id_user_seq'::regclass),
    password character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT user_pkey PRIMARY KEY (id_user)
);

CREATE TABLE IF NOT EXISTS public.antrian
(
    id integer NOT NULL,
    nama_pelanggan character varying(50),
    nomor_antrian integer,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.pembayaran
    ADD CONSTRAINT pembayaran_id_pembeli_fkey FOREIGN KEY (id_pembeli)
    REFERENCES public.pemesanan (id_pembeli) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

END;