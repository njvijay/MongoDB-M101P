import base64

code="CmltcG9ydCBweW1vbmdvCmltcG9ydCB1cmxsaWIyCmltcG9ydCB1cmxsaWIKaW1wb3J0IGNvb2tpZWxpYgppbXBvcnQgcmFuZG9tCmltcG9ydCByZQppbXBvcnQgc3RyaW5nCmltcG9ydCBzeXMKaW1wb3J0IGdldG9wdAoKIyBpbml0IHRoZSBnbG9iYWwgY29va2llIGphcgpjaiA9IGNvb2tpZWxpYi5Db29raWVKYXIoKQojIGRlY2xhcmUgdGhlIHZhcmlhYmxlcyB0byBjb25uZWN0IHRvIGRiCmNvbm5lY3Rpb24gPSBOb25lCmRiID0gTm9uZQp3ZWJob3N0ID0gImxvY2FsaG9zdDo4MDgyIgptb25nb3N0ciA9ICJtb25nb2RiOi8vbG9jYWxob3N0OjI3MDE3IgpkYl9uYW1lID0gImJsb2ciCgojIHRoaXMgc2NyaXB0IHdpbGwgY2hlY2sgdGhhdCBob21ld29yayAzLjIgaXMgY29ycmVjdAoKIyBtYWtlcyBhIGxpdHRsZSBzYWx0CmRlZiBtYWtlX3NhbHQobik6CiAgICBzYWx0ID0gIiIKICAgIGZvciBpIGluIHJhbmdlKG4pOgogICAgICAgIHNhbHQgPSBzYWx0ICsgcmFuZG9tLmNob2ljZShzdHJpbmcuYXNjaWlfbGV0dGVycykKICAgIHJldHVybiBzYWx0CgoKIyB0aGlzIGlzIGEgdmFsaWRhdGlvbiBwcm9ncmFtIHRvIG1ha2Ugc3VyZSB0aGF0IHRoZSBibG9nIHdvcmtzIGNvcnJlY3RseS4KCmRlZiBjcmVhdGVfdXNlcih1c2VybmFtZSwgcGFzc3dvcmQpOgogICAgCiAgICBnbG9iYWwgY2oKCiAgICB0cnk6CiAgICAgICAgcHJpbnQgIlRyeWluZyB0byBjcmVhdGUgYSB0ZXN0IHVzZXIgIiwgdXNlcm5hbWUKICAgICAgICB1cmwgPSAiaHR0cDovL3swfS9zaWdudXAiLmZvcm1hdCh3ZWJob3N0KQoKICAgICAgICBkYXRhID0gdXJsbGliLnVybGVuY29kZShbKCJlbWFpbCIsIiIpLCgidXNlcm5hbWUiLHVzZXJuYW1lKSwgKCJwYXNzd29yZCIscGFzc3dvcmQpLCAoInZlcmlmeSIscGFzc3dvcmQpXSkKICAgICAgICByZXF1ZXN0ID0gdXJsbGliMi5SZXF1ZXN0KHVybD11cmwsIGRhdGE9ZGF0YSkKICAgICAgICBvcGVuZXIgPSB1cmxsaWIyLmJ1aWxkX29wZW5lcih1cmxsaWIyLkhUVFBDb29raWVQcm9jZXNzb3IoY2opKQogICAgICAgIGYgPSBvcGVuZXIub3BlbihyZXF1ZXN0KQoKICAgICAgICB1c2VycyA9IGRiLnVzZXJzCiAgICAgICAgIyBjaGVjayB0aGF0IHRoZSB1c2VyIGlzIGluIHVzZXJzIGNvbGxlY3Rpb24KICAgICAgICB1c2VyID0gdXNlcnMuZmluZF9vbmUoeydfaWQnOnVzZXJuYW1lfSkKICAgICAgICBpZiAodXNlciA9PSBOb25lKToKICAgICAgICAgICAgcHJpbnQgIkNvdWxkIG5vdCBmaW5kIHRoZSB0ZXN0IHVzZXIgIiwgdXNlcm5hbWUsICJpbiB0aGUgdXNlcnMgY29sbGVjdGlvbi4iCiAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgIHByaW50ICJGb3VuZCB0aGUgdGVzdCB1c2VyICIsIHVzZXJuYW1lLCAiIGluIHRoZSB1c2VycyBjb2xsZWN0aW9uIgoKICAgICAgICAjIGNoZWNrIHRoYXQgdGhlIHVzZXIgaGFzIGJlZW4gYnVpbHQKICAgICAgICByZXN1bHQgPSBmLnJlYWQoKQogICAgICAgIGV4cHIgPSByZS5jb21waWxlKCJXZWxjb21lXHMrIisgdXNlcm5hbWUpCiAgICAgICAgaWYgZXhwci5zZWFyY2gocmVzdWx0KToKICAgICAgICAgICAgcmV0dXJuIFRydWUKICAgICAgICAKICAgICAgICBwcmludCAiV2hlbiB3ZSB0cmllZCB0byBjcmVhdGUgYSB1c2VyLCBoZXJlIGlzIHRoZSBvdXRwdXQgd2UgZ290XG4iCiAgICAgICAgcHJpbnQgcmVzdWx0CiAgICAgICAgCiAgICAgICAgcmV0dXJuIEZhbHNlCiAgICBleGNlcHQ6CiAgICAgICAgcHJpbnQgInRoZSByZXF1ZXN0IHRvICIsIHVybCwgIiBmYWlsZWQsIHNvIHlvdXIgYmxvZyBtYXkgbm90IGJlIHJ1bm5pbmcuIgogICAgICAgIHJhaXNlCiAgICAgICAgcmV0dXJuIEZhbHNlCgoKZGVmIHRyeV90b19sb2dpbih1c2VybmFtZSwgcGFzc3dvcmQpOgoKICAgIHRyeToKICAgICAgICBwcmludCAiVHJ5aW5nIHRvIGxvZ2luIGZvciB0ZXN0IHVzZXIgIiwgdXNlcm5hbWUKICAgICAgICB1cmwgPSAiaHR0cDovL3swfS9sb2dpbiIuZm9ybWF0KHdlYmhvc3QpCgogICAgICAgIGRhdGEgPSB1cmxsaWIudXJsZW5jb2RlKFsoInVzZXJuYW1lIix1c2VybmFtZSksICgicGFzc3dvcmQiLHBhc3N3b3JkKV0pCiAgICAgICAgcmVxdWVzdCA9IHVybGxpYjIuUmVxdWVzdCh1cmw9dXJsLCBkYXRhPWRhdGEpCiAgICAgICAgb3BlbmVyID0gdXJsbGliMi5idWlsZF9vcGVuZXIodXJsbGliMi5IVFRQQ29va2llUHJvY2Vzc29yKGNqKSkKICAgICAgICBmID0gb3BlbmVyLm9wZW4ocmVxdWVzdCkKCiAgICAgICAgIyBjaGVjayBmb3Igc3VjY2Vzc2Z1bCBsb2dpbgogICAgICAgIHJlc3VsdCA9IGYucmVhZCgpCiAgICAgICAgZXhwciA9IHJlLmNvbXBpbGUoIldlbGNvbWVccysiKyB1c2VybmFtZSkKICAgICAgICBpZiBleHByLnNlYXJjaChyZXN1bHQpOgogICAgICAgICAgICByZXR1cm4gVHJ1ZQoKICAgICAgICBwcmludCAiV2hlbiB3ZSB0cmllZCB0byBsb2dpbiwgaGVyZSBpcyB0aGUgb3V0cHV0IHdlIGdvdFxuIgogICAgICAgIHByaW50IHJlc3VsdAogICAgICAgIHJldHVybiBGYWxzZQogICAgZXhjZXB0OgogICAgICAgIHByaW50ICJ0aGUgcmVxdWVzdCB0byAiLCB1cmwsICIgZmFpbGVkLCBzbyB5b3VyIGJsb2cgbWF5IG5vdCBiZSBydW5uaW5nLiIKICAgICAgICByZXR1cm4gRmFsc2UKCgpkZWYgYWRkX2Jsb2dfcG9zdCh0aXRsZSxwb3N0LHRhZ3MpOgoKICAgIHRyeToKICAgICAgICBwcmludCAiVHJ5aW5nIHRvIHN1Ym1pdCBhIHBvc3Qgd2l0aCB0aXRsZSAiLCB0aXRsZQogICAgICAgIGRhdGEgPSB1cmxsaWIudXJsZW5jb2RlKFsoImJvZHkiLHBvc3QpLCAoInN1YmplY3QiLHRpdGxlKSwgKCJ0YWdzIix0YWdzKV0pCiAgICAgICAgdXJsID0gImh0dHA6Ly97MH0vbmV3cG9zdCIuZm9ybWF0KHdlYmhvc3QpCiAgICAgICAgcmVxdWVzdCA9IHVybGxpYjIuUmVxdWVzdCh1cmw9dXJsLCBkYXRhPWRhdGEpCiAgICAgICAgY2ouYWRkX2Nvb2tpZV9oZWFkZXIocmVxdWVzdCkKICAgICAgICBvcGVuZXIgPSB1cmxsaWIyLmJ1aWxkX29wZW5lcigpCiAgICAgICAgZiA9IG9wZW5lci5vcGVuKHJlcXVlc3QpCgogICAgICAgICMgY2hlY2sgZm9yIHN1Y2Nlc3NmdWwgbG9naW4KICAgICAgICByZXN1bHQgPSBmLnJlYWQoKQogICAgICAgIGV4cHIgPSByZS5jb21waWxlKHRpdGxlICsgIi4rIiArIHBvc3QsIHJlLkRPVEFMTCkKCiAgICAgICAgaWYgZXhwci5zZWFyY2gocmVzdWx0KToKICAgICAgICAgICAgcmV0dXJuIFRydWUKCiAgICAgICAgcHJpbnQgIldoZW4gd2UgdHJpZWQgdG8gcG9zdCwgaGVyZSBpcyB0aGUgb3V0cHV0IHdlIGdvdFxuIgogICAgICAgIHByaW50IHJlc3VsdAogICAgICAgIHJldHVybiBGYWxzZQoKICAgIGV4Y2VwdDoKICAgICAgICBwcmludCAidGhlIHJlcXVlc3QgdG8gIiwgdXJsLCAiIGZhaWxlZCwgc28geW91ciBibG9nIG1heSBub3QgYmUgcnVubmluZy4iCiAgICAgICAgcmFpc2UKCiAgICAgICAgcmV0dXJuIEZhbHNlCgpkZWYgYWRkX2Jsb2dfY29tbWVudCh0aXRsZSxwb3N0KToKCiAgICB0cnk6CiAgICAgICAgcHJpbnQgIlRyeWluZyB0byBzdWJtaXQgYSBibG9nIGNvbW1lbnQgZm9yIHBvc3Qgd2l0aCB0aXRsZSIsIHRpdGxlCiAgICAgICAgdXJsID0gImh0dHA6Ly97MH0vbmV3Y29tbWVudCIuZm9ybWF0KHdlYmhvc3QpCiAgICAgICAgCiAgICAgICAgZG9jID0ge30KICAgICAgICBjaGVja19tb25nb19mb3JfcG9zdCh0aXRsZSwgcG9zdCwgZG9jKQoKICAgICAgICBwZXJtYWxpbmsgPSBkb2NbJ2RvYyddWydwZXJtYWxpbmsnXQoKICAgICAgICBjb21tZW50X25hbWUgPSBtYWtlX3NhbHQoMTIpCiAgICAgICAgY29tbWVudF9ib2R5ID0gbWFrZV9zYWx0KDEyKQoKICAgICAgICBkYXRhID0gdXJsbGliLnVybGVuY29kZShbKCJjb21tZW50TmFtZSIsY29tbWVudF9uYW1lKSwgKCJjb21tZW50Qm9keSIsY29tbWVudF9ib2R5KSwgKCJwZXJtYWxpbmsiLHBlcm1hbGluayldKQogICAgICAgIHJlcXVlc3QgPSB1cmxsaWIyLlJlcXVlc3QodXJsPXVybCwgZGF0YT1kYXRhKQogICAgICAgIGNqLmFkZF9jb29raWVfaGVhZGVyKHJlcXVlc3QpCiAgICAgICAgb3BlbmVyID0gdXJsbGliMi5idWlsZF9vcGVuZXIoKQogICAgICAgIGYgPSBvcGVuZXIub3BlbihyZXF1ZXN0KQoKICAgICAgICAjIGNoZWNrIGZvciBzdWNjZXNzZnVsIGFkZGl0aW9uIG9mIGNvbW1lbnQgb24gcGFnZQogICAgICAgIHJlc3VsdCA9IGYucmVhZCgpCiAgICAgICAgZXhwciA9IHJlLmNvbXBpbGUodGl0bGUgKyAiLisiICsgcG9zdCwgcmUuRE9UQUxMKQoKICAgICAgICBpZiBub3QgZXhwci5zZWFyY2gocmVzdWx0KToKICAgICAgICAgICAgcHJpbnQgIldoZW4gd2UgdHJpZWQgdG8gZmluZCB0aGUgY29tbWVudCB3ZSBwb3N0ZWQgYXQgdGhlICAiLCB1cmwsICIgaGVyZSBpcyB3aGF0IHdlIGdvdCIKICAgICAgICAgICAgcHJpbnQgcmVzdWx0CiAgICAgICAgICAgIHJldHVybiBGYWxzZQoKCiAgICAgICAgIyBjaGVjayBmb3Igc3VjY2Vzc2Z1bCBhZGRpdGlvbiBvZiBjb21tZW50Li5yZXRyaWV2ZSB0aGUgZG9jIGFnYWluCiAgICAgICAgaWYobm90IGNoZWNrX21vbmdvX2Zvcl9wb3N0KHRpdGxlLCBwb3N0LCBkb2MpKToKICAgICAgICAgICAgcHJpbnQgIkNvdWxkIG5vdCBmaW5kIGNvbW1lbnQgaW4gZGF0YWJhc2UiCiAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgIAogICAgICAgIGZvdW5kID0gRmFsc2UKICAgICAgICBpZiAoJ2NvbW1lbnRzJyBpbiBkb2NbJ2RvYyddKToKICAgICAgICAgICAgZm9yIGNvbW1lbnQgaW4gZG9jWydkb2MnXVsnY29tbWVudHMnXToKICAgICAgICAgICAgICAgIGlmIChjb21tZW50Wydib2R5J10gPT0gY29tbWVudF9ib2R5IGFuZCBjb21tZW50WydhdXRob3InXSA9PSBjb21tZW50X25hbWUpOgogICAgICAgICAgICAgICAgICAgIGZvdW5kID0gVHJ1ZQoKICAgICAgICByZXR1cm4gZm91bmQKCiAgICBleGNlcHQ6CiAgICAgICAgcHJpbnQgInRoZSByZXF1ZXN0IHRvICIsIHVybCwgIiBmYWlsZWQsIHNvIHlvdXIgYmxvZyBtYXkgbm90IGJlIHJ1bm5pbmcuIgogICAgICAgIHJhaXNlCgogICAgICAgIHJldHVybiBGYWxzZQoKCiMgZ3JhYnMgdGhlIGJsb2cgaW5kZXggYW5kIGNoZWNrcyB0aGF0IHRoZSBwb3N0cyBhcHBlYXIgaW4gdGhlIHJpZ2h0IG9yZGVyCmRlZiBjaGVja19ibG9nX2luZGV4KHRpdGxlMSwgdGl0bGUyKToKCiAgICB0cnk6CiAgICAgICAgdXJsID0gImh0dHA6Ly97MH0vIi5mb3JtYXQod2ViaG9zdCkKICAgICAgICBwcmludCAiVHJ5aW5nIHRvIGdyYWIgdGhlIGJsb2cgaG9tZSBwYWdlIGF0IHVybCAiLCB1cmwKICAgICAgICByZXF1ZXN0ID0gdXJsbGliMi5SZXF1ZXN0KHVybD11cmwpCiAgICAgICAgY2ouYWRkX2Nvb2tpZV9oZWFkZXIocmVxdWVzdCkKICAgICAgICBvcGVuZXIgPSB1cmxsaWIyLmJ1aWxkX29wZW5lcigpCiAgICAgICAgZiA9IG9wZW5lci5vcGVuKHJlcXVlc3QpCgogICAgICAgICMgY2hlY2sgZm9yIHN1Y2Nlc3NmdWwgbG9naW4KICAgICAgICByZXN1bHQgPSBmLnJlYWQoKQogICAgICAgIGV4cHIgPSByZS5jb21waWxlKHRpdGxlMiArICIuKyIgKyB0aXRsZTIsIHJlLkRPVEFMTCkKCiAgICAgICAgaWYgZXhwci5zZWFyY2gocmVzdWx0KToKICAgICAgICAgICAgcmV0dXJuIFRydWUKCiAgICAgICAgcHJpbnQgIldoZW4gd2UgdHJpZWQgdG8gcmVhZCB0aGUgYmxvZyBpbmRleCBhdCAiLCB1cmwsICIgaGVyZSBpcyB3aGF0IHdlIGdvdCIKICAgICAgICBwcmludCByZXN1bHQKICAgICAgICByZXR1cm4gRmFsc2UKCiAgICBleGNlcHQ6CiAgICAgICAgcHJpbnQgInRoZSByZXF1ZXN0IHRvICIsIHVybCwgIiBmYWlsZWQsIHNvIHlvdXIgYmxvZyBtYXkgbm90IGJlIHJ1bm5pbmcuIgogICAgICAgIHJhaXNlCgogICAgICAgIHJldHVybiBGYWxzZQoKIyBjaGVjayB0aGF0IGEgcGFydGljdWxhciBibG9nIHBvc3QgaXMgaW4gdGhlIGNvbGxlY3Rpb24KZGVmIGNoZWNrX21vbmdvX2Zvcl9wb3N0KHRpdGxlLCBib2R5LCBkb2N1bWVudCk6CiAgICAKICAgIHBvc3RzID0gZGIucG9zdHMKICAgIHRyeToKICAgICAgICBwb3N0ID0gcG9zdHMuZmluZF9vbmUoeyd0aXRsZSc6dGl0bGUsICdib2R5Jzpib2R5fSkKICAgICAgICBpZiAocG9zdCBpcyBOb25lKToKICAgICAgICAgICAgcHJpbnQgIkNhbid0IGZpbmQgcG9zdCB3aXRoIHRpdGxlICIsIHRpdGxlLCAiIGluIGNvbGxlY3Rpb24iCiAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgIGRvY3VtZW50Wydkb2MnXSA9IHBvc3QKICAgICAgICByZXR1cm4gVHJ1ZQogICAgZXhjZXB0OgogICAgICAgIHByaW50ICJjYW4nIHF1ZXJ5IE1vbmdvREIuLmlzIGl0IHJ1bm5pbmc/IgogICAgICAgIHJhaXNlCgogICAgICAgIHJldHVybiBGYWxzZQoKIyBjb21tYW5kIGxpbmUgYXJnIHBhcnNpbmcgdG8gbWFrZSBmb2xrcyBoYXBweSB3aG8gd2FudCB0byBydW4gYXQgbW9uZ29sYWJzIG9yIG1vbmdvaHEKIyB0aGlzIGZ1bmN0aW9ucyB1c2VzIGdsb2JhbCB2YXJzIHRvIGNvbW11bmljYXRlLiBmb3JnaXZlIG1lLgpkZWYgYXJnX3BhcnNpbmcoYXJndik6CgogICAgZ2xvYmFsIHdlYmhvc3QKICAgIGdsb2JhbCBtb25nb3N0cgogICAgZ2xvYmFsIGRiX25hbWUKCiAgICB0cnk6CiAgICAgICAgb3B0cywgYXJncyA9IGdldG9wdC5nZXRvcHQoYXJndiwgIi1wOi1tOi1kOiIpCiAgICBleGNlcHQgZ2V0b3B0LkdldG9wdEVycm9yOgogICAgICAgIHByaW50ICJ1c2FnZSB2YWxpZGF0ZS5weSAtcCB3ZWJob3N0IC1tIG1vbmdvQ29ubmVjdFN0cmluZyAtZCBkYXRhYmFzZU5hbWUiCiAgICAgICAgcHJpbnQgIlx0d2ViaG9zdCBkZWZhdWx0cyB0byB7MH0iLmZvcm1hdCh3ZWJob3N0KQogICAgICAgIHByaW50ICJcdG1vbmdvQ29ubmVjdGlvblN0cmluZyBkZWZhdWx0IHRvIHswfSIuZm9ybWF0KG1vbmdvc3RyKQogICAgICAgIHByaW50ICJcdGRhdGFiYXNlTmFtZSBkZWZhdWx0cyB0byB7MH0iLmZvcm1hdChkYl9uYW1lKQogICAgICAgIHN5cy5leGl0KDIpCiAgICBmb3Igb3B0LCBhcmcgaW4gb3B0czoKICAgICAgICBpZiAob3B0ID09ICctaCcpOgogICAgICAgICAgICBwcmludCAidXNhZ2UgdmFsaWRhdGUucHkgLXAgd2ViaG9zdCAtbSBtb25nb0Nvbm5lY3RTdHJpbmcgLWQgZGF0YWJhc2VOYW1lIgogICAgICAgICAgICBzeXMuZXhpdCgyKQogICAgICAgIGVsaWYgb3B0IGluICgiLXAiKToKICAgICAgICAgICAgd2ViaG9zdCA9IGFyZwogICAgICAgICAgICBwcmludCAiT3ZlcnJpZGluZyBIVFRQIGhvc3QgdG8gYmUgIiwgd2ViaG9zdAogICAgICAgIGVsaWYgb3B0IGluICgiLW0iKToKICAgICAgICAgICAgbW9uZ29zdHIgPSBhcmcKICAgICAgICAgICAgcHJpbnQgIk92ZXJyaWRpbmcgTW9uZ29EQiBjb25uZWN0aW9uIHN0cmluZyB0byBiZSAiLCBtb25nb3N0cgogICAgICAgIGVsaWYgb3B0IGluICgiLWQiKToKICAgICAgICAgICAgZGJfbmFtZSA9IGFyZwogICAgICAgICAgICBwcmludCAiT3ZlcnJpZGluZyBNb25nb0RCIGRhdGFiYXNlIHRvIGJlICIsIGRiX25hbWUKICAgICAgICAgICAgCgoKIyBtYWluIHNlY3Rpb24gb2YgdGhlIGNvZGUKZGVmIG1haW4oYXJndik6CiAgICAgICAgICAgIAogICAgYXJnX3BhcnNpbmcoYXJndikKICAgIGdsb2JhbCBjb25uZWN0aW9uCiAgICBnbG9iYWwgZGIKCiAgICBwcmludCAiV2VsY29tZSB0byB0aGUgSFcgMy4yIGFuZCBIVyAzLjMgdmFsaWRhdGlvbiB0ZXN0ZXIiCgogICAgIyBjb25uZWN0IHRvIHRoZSBkYiAobW9uZ29zdHIgd2FzIHNldCBpbiBhcmdfcGFyc2luZykKICAgIGNvbm5lY3Rpb24gPSBweW1vbmdvLkNvbm5lY3Rpb24obW9uZ29zdHIsIHNhZmU9VHJ1ZSkKICAgIGRiID0gY29ubmVjdGlvbltkYl9uYW1lXQogICAgICAgIAogICAgdXNlcm5hbWUgPSBtYWtlX3NhbHQoNykKICAgIHBhc3N3b3JkID0gbWFrZV9zYWx0KDgpCgogICAgICMgdHJ5IHRvIGNyZWF0ZSB1c2VyCgogICAgaWYgKGNyZWF0ZV91c2VyKHVzZXJuYW1lLCBwYXNzd29yZCkpOgogICAgICAgIHByaW50ICJVc2VyIGNyZWF0aW9uIHN1Y2Nlc3NmdWwuICIKICAgICAgICAgIyB0cnkgdG8gbG9naW4KICAgICAgICBpZiAodHJ5X3RvX2xvZ2luKHVzZXJuYW1lLCBwYXNzd29yZCkpOgogICAgICAgICAgICBwcmludCAiVXNlciBsb2dpbiBzdWNjZXNzZnVsLiIKICAgICAgICBlbHNlOgogICAgICAgICAgICBwcmludCAiVXNlciBsb2dpbiBmYWlsZWQiCiAgICAgICAgICAgIHByaW50ICJPZGQsIHRoaXMgd2Vla3MncyBjb2RlIHNob3VsZCBkbyB0aGF0IGFzIGdpdmVuIgogICAgICAgICAgICBzeXMuZXhpdCgxKQoKICAgIGVsc2U6CiAgICAgICAgcHJpbnQgIlNvcnJ5LCB5b3UgaGF2ZSBub3Qgc29sdmVkIGl0IHlldC4iCiAgICAgICAgc3lzLmV4aXQoMSkKCgogICAgIyB0cnkgdG8gY3JlYXRlIGEgYmxvZyBwb3N0CiAgICBwb3N0MSA9IG1ha2Vfc2FsdCgzMCkKICAgIHRpdGxlMSA9IG1ha2Vfc2FsdCgzMCkKICAgIHRhZ3MxID0gbWFrZV9zYWx0KDUpICsgIiwgIiArIG1ha2Vfc2FsdCg1KSArICIsICIgKyBtYWtlX3NhbHQoNSkKCgogICAgaWYgKGFkZF9ibG9nX3Bvc3QodGl0bGUxLCBwb3N0MSx0YWdzMSkpOgogICAgICAgIHByaW50ICJTdWJtaXNzaW9uIG9mIHNpbmdsZSBwb3N0IHN1Y2Nlc3NmdWwiCiAgICBlbHNlOgogICAgICAgIHByaW50ICJVbmFibGUgdG8gY3JlYXRlIGEgcG9zdCIKICAgICAgICBzeXMuZXhpdCgxKQoKCiAgICAjIHRyeSB0byBjcmVhdGUgYSBzZWNvbmQgYmxvZyBwb3N0CiAgICBwb3N0MiA9IG1ha2Vfc2FsdCgzMCkKICAgIHRpdGxlMiA9IG1ha2Vfc2FsdCgzMCkKICAgIHRhZ3MyID0gbWFrZV9zYWx0KDUpICsgIiwgIiArIG1ha2Vfc2FsdCg1KSArICIsICIgKyBtYWtlX3NhbHQoNSkKCiAgICBpZiAoYWRkX2Jsb2dfcG9zdCh0aXRsZTIsIHBvc3QyLHRhZ3MyKSk6CiAgICAgICAgcHJpbnQgIlN1Ym1pc3Npb24gb2Ygc2Vjb25kIHBvc3Qgc3VjY2Vzc2Z1bCIKICAgIGVsc2U6CiAgICAgICAgcHJpbnQgIlVuYWJsZSB0byBjcmVhdGUgc2Vjb25kIHBvc3QiCiAgICAgICAgc3lzLmV4aXQoMSkKCiAgICAjIG5vdyBsZXQncyBtYWtlIHN1cmUgdGhhdCBib3RoIHBvc3RzIGFwcGVhciBvbiB0aGUgaG9tZSBwYWdlIG9mIHRoZSBibG9nLCBpbiB0aGUgY29ycmVjdCBvcmRlcgoKICAgIGlmIChjaGVja19ibG9nX2luZGV4KHRpdGxlMSwgdGl0bGUyKSk6CiAgICAgICAgcHJpbnQgIkJsb2NrIGluZGV4IGxvb2tzIGdvb2QuIgogICAgZWxzZToKICAgICAgICBwcmludCAiQmxvZyBpbmRleCBkb2VzIG5vdCBoYXZlIHRoZSBwb3N0cyBwcmVzZW50LCBvcmRlcmVkIGNvcnJlY3RseSIKICAgICAgICBzeXMuZXhpdCgxKQoKCiAgICAjIGNoZWNrIGZvciBEQiBkYXRhIGludGVncml0eQogICAgaWYgKG5vdCBjaGVja19tb25nb19mb3JfcG9zdCh0aXRsZTEsIHBvc3QxLCB7fSkpOgogICAgICAgIHByaW50ICJDYW4ndCBmaW5kIGJsb2cgcG9zdCBpbiBibG9nIGRiLCBwb3N0cyBjb2xsZWN0aW9uIHdpdGggdGl0bGUgIiwgdGl0bGUKICAgICAgICBzeXMuZXhpdCgxKQogICAgZWxzZToKICAgICAgICBwcmludCAiRm91bmQgYmxvZyBwb3N0IGluIHBvc3RzIGNvbGxlY3Rpb24iCgoKICAgIHByaW50ICJUZXN0cyBQYXNzZWQgZm9yIEhXIDMuMi4gWW91ciBIVyAzLjIgdmFsaWRhdGlvbiBjb2RlIGlzIGhqa2ZkNDg5aGprZmhkczg5MzRrZjIzIgoKICAgICMgbm93IGNoZWNrIHRoYXQgeW91IGNhbiBwb3N0IGEgY29tbWVudAogICAgaWYgKG5vdCBhZGRfYmxvZ19jb21tZW50KHRpdGxlMSxwb3N0MSkpOgogICAgICAgIHByaW50ICJDYW4ndCBhZGQgYmxvZyBjb21tZW50cyAoc28gSFcgMy4zIG5vdCB5ZXQgY29tcGxldGUpIgogICAgICAgIHN5cy5leGl0KDEpCiAgICBlbHNlOgogICAgICAgIHByaW50ICJTdWNjZXNzZnVsbHkgYWRkZWQgYmxvZyBjb21tZW50cyIKCgogICAgcHJpbnQgIlRlc3RzIFBhc3NlZCBmb3IgSFcgMy4zLiBZb3VyIEhXIDMuMyB2YWxpZGF0aW9uIGNvZGUgaXMgZGhmcjQ4bmY4OWprMDkzZjlrajBkMmQiCiAgICAKCgoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oc3lzLmFyZ3ZbMTpdKQoKCgoKCgoK"
eval(compile(base64.b64decode(code), "<string>", 'exec'))



