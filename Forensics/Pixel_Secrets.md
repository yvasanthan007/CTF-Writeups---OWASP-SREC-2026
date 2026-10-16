# Pixel Secrets

- **Event:** OWASP CTF
- **Category:** Forensics
- **Tool Used:** Aperi'Solve
- **Technique:** Image Steganography Analysis using zsteg

## Objective

The challenge involved analyzing a provided sunset image to find a hidden flag. The objective was to examine the image using forensic techniques and recover the concealed information.

## Approach and Methodology

I used the online tool Aperi'Solve to analyze the given image. During the analysis, I used its `zsteg` functionality to inspect the image for hidden data. This helped me identify the concealed flag within the image.

## Result

Successfully analyzed the image and recovered the hidden flag.

**Flag:** `OWASP{50_l1ttl3_b1ts_h1d3_b1g_s3cr3t5}`

## Learning Outcome

This challenge helped me understand how information can be concealed within image files using steganography. I learned how Aperi'Solve and its `zsteg` functionality can assist in analyzing images and detecting hidden data during digital forensics investigations.

## Tool Reference

[Aperi'Solve](https://www.aperisolve.com/)