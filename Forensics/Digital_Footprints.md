# Digital Footprints

- **Event:** OWASP CTF
- **Category:** Forensics
- **Tools Used:** Aperi'Solve, CyberChef
- **Technique:** Image Metadata Analysis and Hexadecimal Decoding

## Objective

The challenge involved finding a hidden flag within the metadata of a provided vacation image. The objective was to inspect the image metadata, identify the hidden information, and reconstruct the flag.

## Approach and Methodology

I used Aperi'Solve to analyze the provided image and examine its metadata. During the analysis, I found three separate pieces of flag information: two represented as hexadecimal values and one provided as plain text. I used CyberChef to decode the hexadecimal values and combined the recovered information to identify the complete flag.

## Result

Successfully analyzed the image metadata, decoded the hexadecimal values, and recovered the flag.

**Flag:** `OWASP{m3t4d4t4_t3ll3s_all_s3cr3t5}`

## Learning Outcome

This challenge helped me understand the importance of image metadata in digital forensics and how it can contain hidden information. I learned to use Aperi'Solve to inspect image metadata and CyberChef to decode hexadecimal data, helping me recover information concealed within a file.

## Tool Reference

- [Aperi'Solve](https://www.aperisolve.com/)
- [CyberChef](https://gchq.github.io/CyberChef/)