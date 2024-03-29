
html_template = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Email Template</title>
  </head>

  <body style="margin: 0; padding: 0">
    <table
      align="center"
      border="0"
      cellpadding="0"
      cellspacing="0"
      width="600"
    >
      <tr>
        <td align="center" bgcolor="#ffffff" style="padding: 40px 0 0">
          <img
            src="{header}"
            alt=""
            style="
              display: block;
              border: 0;
              outline: none;
              text-decoration: none;
              -ms-interpolation-mode: bicubic;
            "
            width="600"
            height="161"
          />
        </td>
      </tr>
      <tr>
        <td
          style="
            padding: 40px;
            margin: 0;
            background-color: #fff;
            color: #000;
            background-position: left center;
            background-repeat: no-repeat;
          "
          bgcolor="#d8d8d8"
          align="left"
        >
          <table
            width="100%"
            cellspacing="0"
            cellpadding="0"
            role="none"
            style="
              mso-table-lspace: 0pt;
              mso-table-rspace: 0pt;
              border-collapse: collapse;
              border-spacing: 0px;
            "
          >
            <tr>
              <td
                valign="top"
                align="center"
                style="padding: 0; margin: 0; width: 520px"
              >
                <table
                  style="
                    mso-table-lspace: 0pt;
                    mso-table-rspace: 0pt;
                    border-collapse: collapse;
                    border-spacing: 0px;
                    background-color: transparent;
                    background-position: left top;
                  "
                  width="100%"
                  cellspacing="0"
                  cellpadding="0"
                  bgcolor="transparent"
                  role="presentation"
                >
                  <tr>
                    <td align="left" style="padding: 0; margin: 0; color: #000">
                      <h2
                        style="
                          margin: 0;
                          line-height: 43px;
                          mso-line-height-rule: exactly;
                          font-family: 'Space Grotesk', sans-serif;
                          font-size: 16px;
                          font-style: normal;
                          font-weight: normal;
                        "
                      >
                        Hi <strong>{name}</strong>,
                       </h2>
                     <p style="
                              margin: 0;
                              -webkit-text-size-adjust: none;
                              -ms-text-size-adjust: none;
                              mso-line-height-rule: exactly;
                              line-height: 22px;
                              font-size: 16px;
                              color: #000;
                              white-space: pre-wrap;
                              ">
                          <span style="display: inline-block; text-indent: -2em;">{emailContent}</span>
                          <br />
                      </p>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="padding: 0; margin: 0; color: #000">
                      <p
                        style="
                          olor: #000;
                          margin: 0;
                          -webkit-text-size-adjust: none;
                          -ms-text-size-adjust: none;
                          mso-line-height-rule: exactly;
                          font-family: lato, 'helvetica neue', helvetica, arial,
                            sans-serif;
                          line-height: 24px;
                          font-size: 16px;
                        "
                      >
                        <br />
                      </p>
                      <p
                        style="
                          color: #000;
                          margin: 0;
                          -webkit-text-size-adjust: none;
                          -ms-text-size-adjust: none;
                          mso-line-height-rule: exactly;
                          font-family: lato, 'helvetica neue', helvetica, arial,
                            sans-serif;
                          line-height: 24px;
                          font-size: 16px;
                        "
                      >
                        Regards,
                        <br />
                        <strong>{company}</strong>
                      </p>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr>
        <td
          style="
            padding-top: 25px;
            padding-bottom: 55px;
            margin: 0;
            background-color: #000;
            color: #fff;
          "
        >
          <table
            width="100%"
            cellspacing="0"
            cellpadding="0"
            role="none"
            style="
              mso-table-lspace: 0pt;
              mso-table-rspace: 0pt;
              border-collapse: collapse;
              border-spacing: 0px;
            "
          >
            <tr>
              <td
                valign="top"
                align="center"
                style="padding: 0; margin: 0; width: 520px"
              >
                <table
                  style="
                    mso-table-lspace: 0pt;
                    mso-table-rspace: 0pt;
                    border-collapse: collapse;
                    border-spacing: 0px;
                    background-color: transparent;
                    background-position: left top;
                  "
                  width="100%"
                  cellspacing="0"
                  cellpadding="0"
                  bgcolor="transparent"
                  role="presentation"
                >
                  <tr>
                    <td
                      align="center"
                      style="
                        padding: 0;
                        margin: 0;
                        padding-bottom: 5px;
                        padding-left: 20px;
                        padding-right: 20px;
                      "
                    ></td>
                  </tr>
                  <tr>
                    <td
                      align="center"
                      style="padding: 0; margin: 0; font-size: 0"
                    ></td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>

"""