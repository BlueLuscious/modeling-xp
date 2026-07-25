/**
 * Toggle Display Password:
 * @param {Object} password_input Input.
 * @param {Object} eye_icon Eye Icon.
 * @param {Object} eye_slash_icon Eye Slash Icon.
 * @returns {void} None.
 */
export function toggleDisplayPassword(password_input_id, eye_icon_id, eye_slash_icon_id) {
    const passwordInput = document.getElementById(password_input_id)
    const eyeIcon = document.getElementById(eye_icon_id)
    const eyeSlashIcon = document.getElementById(eye_slash_icon_id)

    const isPassword = passwordInput.type === "password"
    passwordInput.type = isPassword ? "text" : "password"

    eyeIcon.classList.toggle("hidden", isPassword)
    eyeSlashIcon.classList.toggle("hidden", !isPassword)
}
