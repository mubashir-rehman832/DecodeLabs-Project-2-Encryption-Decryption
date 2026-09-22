
import streamlit as st


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Cryptographic Lab | DecodeLabs",
    page_icon="🔐",
    layout="wide"
)


# ==================================================
# CAESAR CIPHER FUNCTIONS
# ==================================================

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char

    return result


# ==================================================
# HEADER
# ==================================================

st.title("Cryptographic Lab")

st.subheader("DecodeLabs Cyber Security — Project 2")

st.write(
    "Basic Encryption & Decryption using the Caesar Cipher"
)

st.divider()


# ==================================================
# INTRODUCTION
# ==================================================

st.info(
    """
    🛡️ **Secure Your Message**

    This educational cryptographic tool demonstrates the basic
    principles of data confidentiality using the Caesar Cipher.

    Enter a message, select a shift key, and transform your text
    through reversible encryption and decryption logic.
    """
)


# ==================================================
# MESSAGE CONFIGURATION
# ==================================================

st.header("📝 Message Configuration")

col1, col2 = st.columns([3, 1])


with col1:

    text = st.text_area(
        "Message",
        placeholder="Enter the text you want to encrypt or decrypt...",
        height=180
    )


with col2:

    st.subheader("🔑 Shift Key")

    shift = st.number_input(
        "Select shift value",
        min_value=1,
        max_value=25,
        value=3,
        step=1
    )

    st.caption("Choose a value between 1 and 25.")


st.divider()


# ==================================================
# OPERATIONS
# ==================================================

st.header("⚡ Cryptographic Operations")

col1, col2 = st.columns(2)


with col1:

    encrypt_button = st.button(
        "🔒 Encrypt Message",
        use_container_width=True
    )


with col2:

    decrypt_button = st.button(
        "🔓 Decrypt Message",
        use_container_width=True
    )


# ==================================================
# ENCRYPTION OUTPUT
# ==================================================

if encrypt_button:

    if text.strip():

        encrypted_text = encrypt(text, int(shift))

        st.success("Encryption completed successfully.")

        st.subheader("🔒 Encrypted Output")

        st.code(
            encrypted_text,
            language="text"
        )

        st.caption(
            f"Caesar Cipher | Shift Key: {int(shift)}"
        )

    else:

        st.warning(
            "Please enter a message before encryption."
        )


# ==================================================
# DECRYPTION OUTPUT
# ==================================================

if decrypt_button:

    if text.strip():

        decrypted_text = decrypt(text, int(shift))

        st.success("Decryption completed successfully.")

        st.subheader("🔓 Decrypted Output")

        st.code(
            decrypted_text,
            language="text"
        )

        st.caption(
            f"Caesar Cipher | Shift Key: {int(shift)}"
        )

    else:

        st.warning(
            "Please enter a message before decryption."
        )


# ==================================================
# ABOUT THE ALGORITHM
# ==================================================

st.divider()

st.header("📚 About the Caesar Cipher")

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        """
        **🔐 Encryption**

        Characters are shifted forward according
        to the selected shift key.
        """
    )


with col2:

    st.markdown(
        """
        **🔓 Decryption**

        Characters are shifted backward using
        the same shift key.
        """
    )


with col3:

    st.markdown(
        """
        **🛡️ Purpose**

        Demonstrates basic encryption, decryption,
        and data confidentiality concepts.
        """
    )


# ==================================================
# SECURITY NOTE
# ==================================================

with st.expander("⚠️ Security Note"):

    st.write(
        "The Caesar Cipher is an educational encryption technique "
        "and should not be used to protect real confidential information."
    )

    st.write(
        "Modern applications use stronger cryptographic algorithms "
        "to protect sensitive data."
    )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "DecodeLabs Cyber Security — Project 2 | Basic Encryption & Decryption"
)

